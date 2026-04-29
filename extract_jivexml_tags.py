import argparse
import csv
import os
import sys
import xml.etree.ElementTree as ET


def extract_top_level_tag_info(xml_path):
    if not os.path.isfile(xml_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {xml_path}")

    context = ET.iterparse(xml_path, events=("start", "end"))
    root = None
    stack = []

    for event, elem in context:
        if event == "start":
            if root is None:
                root = elem
            stack.append(elem)
            continue

        if len(stack) == 2 and stack[0] is root and stack[-1] is elem:
            subtags = []
            seen = set()
            for child in elem:
                if child.tag not in seen:
                    subtags.append(child.tag)
                    seen.add(child.tag)

            yield {
                "tag": elem.tag,
                "storeGateKey": elem.get("storeGateKey", ""),
                "count": elem.get("count", ""),
                "subtags": subtags,
            }

            elem.clear()

        stack.pop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrai tags JiveXML para CSV organizado.")
    parser.add_argument("xml_file", help="Caminho do arquivo JiveXML")
    parser.add_argument("output_csv", nargs="?", default="tags.csv", help="Arquivo CSV de saída")
    args = parser.parse_args()

    try:
        rows = list(extract_top_level_tag_info(args.xml_file))
    except (ET.ParseError, FileNotFoundError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        sys.exit(1)

    max_subtags = max((len(row["subtags"]) for row in rows), default=0)
    headers = ["tag", "storeGateKey", "count"] + [f"subtag_{i}" for i in range(max_subtags)]

    with open(args.output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=";")
        writer.writeheader()
        for row in rows:
            line = {"tag": row["tag"], "storeGateKey": row["storeGateKey"], "count": row["count"]}
            line.update({f"subtag_{i}": subtag for i, subtag in enumerate(row["subtags"])})
            writer.writerow(line)

    print(f"Extração concluída: {args.output_csv} ({len(rows)} registros)")

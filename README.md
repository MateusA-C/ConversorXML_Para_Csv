# ConversorXMLparaCSV

Este script Python lê arquivos JiveXML e extrai informações das tags de nível superior, incluindo `storeGateKey`, `count` e subtags, gerando um arquivo CSV organizado.

## Funcionalidades

- Processa arquivos JiveXML de qualquer tamanho de forma eficiente usando iterparse.
- Extrai tags principais com seus atributos.
- Lista subtags únicas para cada tag principal.
- Gera CSV com colunas dinâmicas para subtags.

## Requisitos

- Python 3.6 ou superior instalado.
- Nenhum pacote adicional necessário (usa apenas bibliotecas padrão do Python).

## Como Usar

1. Certifique-se de que o Python está instalado. Verifique com `python --version`.

2. Navegue até o diretório do projeto no terminal:

   ```powershell
   cd c:\Users\mateu\Desktop\ConversorXMLparaCSV
   ```

3. Execute o script fornecendo o caminho do arquivo XML e opcionalmente o nome do arquivo CSV de saída:

   ```powershell
   python extract_jivexml_tags.py "caminho\para\arquivo.xml" "saida.csv"
   ```

   - Se não especificar o CSV de saída, será usado "tags.csv" por padrão.
   - Exemplo:

     ```powershell
     python extract_jivexml_tags.py "JiveXML_519157_1891736366 (1) (1).xml" "meu_tags.csv"
     ```

4. O arquivo CSV será criado no diretório atual.

## Estrutura da Saída CSV

O CSV gerado terá as seguintes colunas:

- `tag`: Nome da tag principal.
- `storeGateKey`: Valor do atributo storeGateKey (se presente).
- `count`: Valor do atributo count (se presente).
- `subtag_0`, `subtag_1`, etc.: Subtags únicas encontradas, cada uma em sua coluna.

## Exemplo de Uso

Supondo que você tenha um arquivo `exemplo.xml`, execute:

```powershell
python extract_jivexml_tags.py exemplo.xml
```

Isso criará `tags.csv` com os dados extraídos.

## Observações

- O script processa o XML de forma streaming, adequado para arquivos grandes.
- Subtags duplicadas são removidas para evitar repetições.
- Se o arquivo XML não for encontrado, o script exibirá um erro.

## Contribuição

Sinta-se à vontade para melhorar o script ou o README.
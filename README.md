# indicium

## Arquivos

Abandono_teste.csv: exemplo usado para o teste do modelo.
indicium.ipynb: notebook com o passo a passo para criação do modelo.
modelo.pkl: o modelo final usado
predict.py: o script que carrega o pkl do modelo, lê o csv de entrada
e salva as previsões em um .csv de saída.
requirements.txt: para facilitar a reprodução do código esse arquivo
contêm a saída do pip freeze (ou seja as bibliotecas usadas e suas
respectivas versões)

## Usando o código

1. Crie um virtual env e instale as bibliotecas no requirements.txt
2. Execute o predict.py passando o nome do arquivo de entrada. Exemplo:
python predict.py Abandono_teste.csv. O resultado vai ser salvo em um csv
chamado saida.csv.

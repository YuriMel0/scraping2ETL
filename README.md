![windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![scrapy](https://img.shields.io/badge/Scrapy-60A839?style=for-the-badge&logo=scrapy&logoColor=white)

# Projeto de Engenharia de Dados: Análise de Tênis de Corrida Masculino no Mercado Livre
Este projeto é uma solução completa de engenharia de dados desenvolvida para extrair, processar e visualizar dados de tênis de corrida masculino disponíveis no Mercado Livre. Utilizando tecnologias como Python, Scrapy, Pandas, SQLite3 e Streamlit, o objetivo é fornecer insights através de um dashboard.

## Tecnologias Utilizadas
- Python: Linguagem principal utilizada no desenvolvimento do projeto.
- Scrapy: Utilizado para realizar o scraping dos dados diretamente do site do Mercado Livre.
- Pandas: Responsável pelo tratamento e análise dos dados extraídos.
- SQLite3: Banco de dados relacional utilizado para armazenar os dados tratados.
- Streamlit: Ferramenta utilizada para a criação de um dashboard interativo, onde os dados são visualizados de forma dinâmica.
## Descrição do Projeto
Coleta de Dados: Utilizando o Scrapy, os dados foram coletados diretamente da busca por "tênis de corrida masculino" no Mercado Livre. Informações como nome do produto, preço, avaliação, e link foram extraídas para análise.

1. Tratamento de Dados: Os dados coletados passaram por um processo de limpeza e tratamento utilizando a biblioteca Pandas, onde foram removidos dados duplicados, tratados valores nulos, e padronizadas as colunas.

2. Armazenamento: Após o tratamento, os dados foram armazenados em um banco de dados SQLite3, facilitando a consulta e manipulação.

3. Visualização: Utilizando o Streamlit, foi desenvolvido um dashboard que permite a visualização dos principais insights sobre os produtos coletados, como distribuições de preços, avaliações médias, entre outros.

## Como Executar o Projeto

Clone este repositório:

`git clone https://github.com/YuriMel0/scraping2ETL`

Navegue até o diretório do projeto:

`cd scraping2ETL/`

Crie e ative o ambiente virtual venv:

`python -m venv venv #Para criar`


`source .venv/bin/activate  #No Windows, para executar venv\Scripts\activate`

Instale as dependências necessárias:

`pip install -r requirements.txt`

Execute o Scrapy para coletar os dados:

`scrapy crawl mercadolivre`

Inicie o Streamlit para visualizar o dashboard:

`streamlit run src/dashboard/app.py`


### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias ou correções.

#  Desafio Técnico – Infomaz 

Análise de dados para o estudo de caso proposto pela Infomaz, com foco em pipeline de ingestão, transformação e visualização usando Python, Meltano, Docker e Jupyter.

## Tecnologias

- Python (Version **3.13.1**)
- Meltano (Version **3.6.0**)
- Docker (Version **27.3.1**)
- Jupyter Client (Version **8.6.3**)
- PostgresSQL (Version **14.15.0**)

## Instalação

1. Clone o repositório

```bash
git clone git@github.com:douglasmnegri/infomaz-case.git
cd infomaz-case
```

2. Python Environment (Recomendado)

```bash
python3 -m venv venv_nome
source venv_nome/bin/activate  # macOS/Linux
```

3. Instale as dependências através do requirements.txt 

```bash
pip install -r requirements.txt
```

4. Configuração do Meltano

```bash
  meltano install
```

## Inicializando o Projeto

1. Partindo do diretório raíz (infomaz-case) execute docker-compose.yml que contém base de dados do projeto:

```bash
docker-compose up -d
```

2. Execute o pipeline de ingestão de dados (ELT):

```bash
meltano run load-all-csv
```

3. Converta os valores numéricos para o formato correto com o script de transformação:
   
```bash
   python3 transform/clean_values.py
```

4. Inicialize o Jupyter Notebook

```bash
jupyter notebook notebook/infomaz_analysis.ipynb
```

5. Acesse o dashboard no navegador:
- 🔗 http://localhost:8888/notebooks/infomaz_analysis.ipynb

## Considerações

Para este desafio, optei por estruturar uma pipeline de dados que permitisse organizar e carregar as informações do estudo de caso em um banco de dados relacional. Essa abordagem busca simular um ambiente real de projetos em produção, onde os dados de entrada, muitas vezes em planilhas, podem passar por alterações ou atualizações ao longo do tempo.

Com essa estrutura, qualquer modificação nos dados de origem pode ser facilmente refletida nas análises finais por meio da simples execução do pipeline ETL. Isso proporciona maior flexibilidade e escalabilidade para o processo de análise!
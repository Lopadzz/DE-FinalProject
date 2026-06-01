# DE Final Project

## Descrição do Projeto

Este projeto utiliza o dataset **Bank Marketing (dirty version)** fornecido na unidade curricular.

O objetivo foi aplicar técnicas de Data Engineering para limpeza, transformação e carregamento dos dados para uma base de dados PostgreSQL executada em containers Docker.

---

## Dataset

Dataset utilizado:

* Bank Marketing Dataset (dirty version)

Características principais:

* Aproximadamente 45.000 registos
* Informação demográfica dos clientes
* Informação sobre campanhas de marketing bancário
* Resultado da subscrição de depósito a prazo (`y`)

---

## Tecnologias Utilizadas

* Docker Compose
* PostgreSQL
* Adminer
* Python
* Pandas
* SQL

---

## Processo de Limpeza dos Dados

Foram executadas as seguintes tarefas:

1. Carregamento do dataset original com Pandas.
2. Normalização dos nomes das colunas.
3. Substituição de indicadores de valores em falta (`unknown`, `N/A` e valores vazios).
4. Remoção de registos duplicados.
5. Preenchimento de valores numéricos em falta através da mediana.
6. Preenchimento de valores categóricos em falta através da moda.
7. Criação de um novo dataset limpo.
8. Carregamento dos dados para PostgreSQL.

---

## Ambiente de Base de Dados

A infraestrutura foi criada utilizando Docker Compose.

Serviços utilizados:

* PostgreSQL 15
* Adminer

Configuração:

* Base de dados: `bankdb`
* Utilizador: `admin`

---

## Ingestão de Dados

O dataset limpo foi carregado para PostgreSQL através de Python, Pandas e SQLAlchemy.

Tabela criada:

* `bank_marketing`

Número de registos:

* Aproximadamente 45.000 linhas

---

## Análise SQL

Foram desenvolvidas várias consultas SQL para análise dos dados, incluindo:

* Número total de clientes
* Distribuição de clientes por estado civil
* Distribuição de clientes por profissão
* Resultado das campanhas de marketing
* Saldo médio por profissão
* Idade média por estado civil
* Clientes com maiores saldos
* Número de contactos por mês
* Estatísticas de campanhas
* Taxa de subscrição por profissão

---

## Estrutura do Projeto

DE-FinalProject/

├── data/

│   ├── bank-marketing-dirty.csv

│   └── bank-marketing-clean.csv

├── scripts/

│   └── load_data.py

├── sql/

│   ├── analysis_queries.sql

│   └── analysis_results.md

├── docker-compose.yml

└── README.md

---

## Resultado Final

O dataset original foi limpo, transformado e carregado com sucesso para PostgreSQL.

As consultas SQL permitiram validar a qualidade dos dados e obter informação relevante sobre os clientes e os resultados das campanhas de marketing bancário.

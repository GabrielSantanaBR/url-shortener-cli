# URL Shortener API

REST API para encurtamento de URLs construída com **Python**, **FastAPI** e **SQLite**. O projeto demonstra criação de endpoints, validação de dados, persistência e documentação automática de API.

## Funcionalidades

- Criar URLs curtas
- Recuperar a URL original
- Redirecionar usando o código curto
- Contabilizar acessos
- Listar URLs cadastradas
- Excluir URLs
- Persistir dados com SQLite
- Explorar e testar endpoints pelo Swagger/OpenAPI do FastAPI

## Tecnologias

Python 3 · FastAPI · SQLite · Pydantic · Uvicorn

## Executando localmente

```bash
git clone https://github.com/GabrielSantanaBR/url-shortener-api.git
cd url-shortener-api
pip install -r requirements.txt
uvicorn api:app --reload
```

API: `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

## Endpoints

| Método | Endpoint | Finalidade |
|---|---|---|
| POST | `/shorten` | Criar uma URL curta |
| GET | `/urls` | Listar URLs armazenadas |
| GET | `/url/{code}` | Consultar uma URL pelo código |
| GET | `/r/{code}` | Redirecionar para a URL original |
| DELETE | `/urls/{code}` | Excluir uma URL curta |

Exemplo de criação:

```json
{
  "url": "https://www.example.com"
}
```

## O que este projeto demonstra

- Design de REST APIs
- Rotas e códigos HTTP
- Validação de entrada com Pydantic
- Persistência em banco relacional
- Separação entre API e camada de dados
- Documentação automática com OpenAPI
- Testes de comportamento de endpoints

## Estrutura

```text
url-shortener-api/
├── api.py
├── database.py
├── main.py
├── requirements.txt
├── tests/
└── README.md
```

## Objetivo

Projeto de portfólio criado para praticar backend em Python e fundamentos de APIs. Ele complementa projetos maiores do portfólio ao mostrar uma implementação menor, focada e fácil de inspecionar.

## Autor

Gabriel Santana — Software, Dados e Automação.

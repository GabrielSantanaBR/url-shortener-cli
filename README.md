# URL Shortener API

A simple URL Shortener API built with **Python**, **FastAPI**, and **SQLite**.

## Features

* Create short URLs
* Retrieve original URLs
* Redirect using short codes
* Count URL accesses
* Delete URLs
* Store data using SQLite

## Technologies

* Python 3
* FastAPI
* SQLite
* Pydantic
* Uvicorn

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/url-shortener-cli.git
```

Enter the project folder:

```bash
cd url-shortener-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn api:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### POST /shorten

Create a short URL.

Example:

```json
{
  "url": "https://www.google.com"
}
```

### GET /urls

List all stored URLs.

### GET /url/{code}

Get information about a short URL.

### GET /r/{code}

Redirect to the original URL.

### DELETE /urls/{code}

Delete a short URL.

## Project Structure

```
url-shortener-cli/
│
├── api.py
├── database.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── urls.db
└── tests/
```

## Author

Developed as a portfolio project to practice Python, FastAPI, REST APIs, and SQLite.

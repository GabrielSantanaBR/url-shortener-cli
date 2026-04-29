# URL Shortener CLI

A simple command-line URL shortener built with Python.
This project allows users to shorten long URLs, store them locally, and retrieve them using a generated code.

## Features

* Shorten long URLs
* Store URLs locally (JSON)
* Retrieve original URLs using a short code
* Simple and interactive CLI interface

## Technologies Used

* Python
* JSON (for local storage)
* Standard libraries (`os`, `random`, `string`)

## Project Structure

```
url-shortener-cli/
│
├── main.py
├── urls.json
└── README.md
```

## How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/url-shortener-cli.git
```

2. Navigate to the project folder:

```
cd url-shortener-cli
```

3. Run the program:

```
python main.py
```

## Example Usage

```
[1] Shorten URL
[2] List URLs
[3] Find URL
[4] Exit

Choose an option: 1
Enter URL: https://example.com/very/long/link

Short URL: abc123
```

## Future Improvements

* URL validation
* Delete and edit links
* Track usage (click counter)
* QR code generation

## Author

Gabriel Santana

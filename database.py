import sqlite3


def get_connection():
    connection = sqlite3.connect("urls.db")
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            code TEXT PRIMARY KEY,
            url TEXT NOT NULL,
            clicks INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def add_url(code, url):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INFO urls (code, url, clicks) VALUES (?, ?, ?)",
        (code, url, 0)
    )

    connection.commit()
    connection.close()

def get_all_urls():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM urls")

    rows = cursor.fetchall()

    connection.close()
    return rows


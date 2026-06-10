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
        "INSERT INTO urls (code, url, clicks) VALUES (?, ?, ?)",
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

def get_url_by_code(code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM urls WHERE code = ?", (code,))

    rows = cursor.fetchall()
    connection.close()

    return rows

def increment_clicks(code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE urls SET clicks = clicks + 1 WHERE code = ?", (code,)
    )

    connection.commit()
    connection.close()

def delete_url_db(code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM urls WHERE clicks = ?", (code,)
    )

    connection.commit()
    connection.close()

def code_exists(code):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM urls WHERE code = ?", (code,))

    result = cursor.fetchome()

    connection.close()

    return result is not None


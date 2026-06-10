import sqlite3

connection = sqlite3.connect("urls.db")
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
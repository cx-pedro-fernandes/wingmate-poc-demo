import sqlite3


def find_customer(name):
    db = sqlite3.connect(":memory:")
    try:
        db.executescript("CREATE TABLE customers (id INTEGER, name TEXT);"
                         "INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob');")
        query = "SELECT id, name FROM customers WHERE name = ?"
        return db.execute(query, (name,)).fetchall()
    finally:
        db.close()

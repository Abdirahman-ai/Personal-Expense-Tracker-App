""""
Created on 06.12.2020 
Database Connection
:author: Abdinahman
"""""
import os
import sqlite3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")


def get_connection():
    return sqlite3.connect(DB_PATH)

def create_expenses_table():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                payment_method TEXT NOT NULL
            )
        """)
        connection.commit()
        print("Expenses Table Created")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        connection.rollback()
    finally:
        connection.close()

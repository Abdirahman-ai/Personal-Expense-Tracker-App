"""
Created on 06.12.2026
Database Connection
:author: Abdinahman
"""
"""
Database connection utility.

This file has two jobs:
1. setup() creates the database and expenses table.
2. get_connection() returns a reusable database connection for the repository layer.
"""

import mysql.connector

def setup():
    try:
        print("Connecting to MySQL...")

        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="NewPassword123!"
        )

        print("Connected.")

        cursor = conn.cursor()

        print("Creating database...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker_db")
        print("Database created.")

        print("Using database...")
        cursor.execute("USE expense_tracker_db")
        print("Database selected.")

        print("Creating table...")
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS expenses (
                            id SERIAL PRIMARY KEY,
                            title TEXT NOT NULL,
                            category TEXT NOT NULL,
                            amount FLOAT NOT NULL,
                            date DATE NOT NULL,
                            payment_method TEXT NOT NULL
                       )
                       """)

        print("Table created.")

        conn.commit()
        

        cursor.close()
        conn.close()

        print("Database setup complete!")

    except Exception as e:
        print(f"ERROR: {e}")

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="NewPassword123!",
        database="expense_tracker_db"
    )
"""
SQL database operations
"""

import mysql.connector

from database.connection import get_connection
from models.expense import Expense


class ExpenseRepository:

    def add_expense(self, expense):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                           INSERT INTO expenses (title, category, amount, date, payment_method)
                           VALUES (%s, %s, %s, %s, %s)
                           """, (
                               expense.title,
                               expense.category,
                               expense.amount,
                               expense.date,
                               expense.payment_method
                           ))

            conn.commit()
            print("Expense added")

        except mysql.connector.Error as error:
            print(f"Insertion database error: {error}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def get_all_expenses(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM expenses")
            rows = cursor.fetchall()

            expenses_table = []

            for row in rows:
                expense = Expense(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )
                expenses_table.append(expense)

            return expenses_table

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            return []

        finally:
            cursor.close()
            conn.close()

    def get_expense_by_id(self, expense_id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM expenses WHERE id = %s",
                (expense_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Expense(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            return None

        finally:
            cursor.close()
            conn.close()

    def get_expense_by_title(self, expense_title):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM expenses WHERE title = %s",
                (expense_title,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Expense(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            return None

        finally:
            cursor.close()
            conn.close()

    def delete_expense_by_id(self, expense_id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM expenses WHERE id = %s",
                (expense_id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                print("No expense found with that ID")
            else:
                print("Expense deleted")

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def update_expense_by_id(self, expense_id, expense):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                           UPDATE expenses
                           SET title = %s,
                               category = %s,
                               amount = %s,
                               date = %s,
                               payment_method = %s
                           WHERE id = %s
                           """, (
                               expense.title,
                               expense.category,
                               expense.amount,
                               expense.date,
                               expense.payment_method,
                               expense_id
                           ))

            conn.commit()

            if cursor.rowcount == 0:
                print("No expense found with that ID")
            else:
                print("Expense updated")

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def delete_expense_by_title(self, expense_title):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM expenses WHERE title = %s",
                (expense_title,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                print("No expense found with that title")
            else:
                print("Expense deleted")

        except mysql.connector.Error as error:
            print(f"Expenses database error: {error}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()
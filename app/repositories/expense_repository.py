"""""
 SQL database operations
"""""
import sqlite3

from database.connection import create_expenses_table, get_connection
from models.expense import Expense

class ExpenseRepository:

    def add_expense(self, expense):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO expenses (title, category, amount, date, payment_method) values (?, ?, ?, ?, ?)""",(
                expense.title,
                expense.category,
                expense.amount,
                expense.date,
                expense.payment_method
            ))
            conn.commit()
        except sqlite3.Error as error:
            print(f"insertion database Error: {error}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def get_all_expenses(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM expenses")

            expenses = cursor.fetchall()
            expenses_table = []
            for expense in expenses:
                exp = Expense(
                    expense[0],
                    expense[1],
                    expense[2],
                    expense[3],
                    expense[4],
                    expense[5],
                )
                expenses_table.append(exp)
            return expenses
        except sqlite3.Error as error:
           print(f"expenses database Error: {error}")
           return []
        finally:
           cursor.close()
           conn.close()

    def get_expense_by_id(self, expense_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM expenses WHERE id = ?",(expense_id,))
            expense = cursor.fetchone()
            return expense
        except sqlite3.Error as error:
            print(f"expenses database Error: {error}")
        finally:
            cursor.close()
            conn.close()

    def get_expense_by_title(self, expense_title):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM expenses WHERE title = ?",(expense_title,))
            expense = cursor.fetchone()
            return expense
        except sqlite3.Error as error:
            print(f"expenses database Error: {error}")
            return []
        finally:
            cursor.close()
            conn.close()

    def delete_expense_by_id(self, expense_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM expenses WHERE id = ?",(expense_id,))
            conn.commit()
            print("expenses deleted")
        except sqlite3.Error as error:
            print(f"expenses database Error: {error}")
        finally:
            cursor.close()
            conn.close()

    def update_expense_by_id(self, expense_id, expense):
        """"
        DON'T FORGET TO CHECK IF ID IS AVAILABLE IN DATABASE 
        """""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("UPDATE expenses SET title = ? WHERE id = ?",(expense.title, expense_id))
            conn.commit()
            print("expenses updated")
        except sqlite3.Error as error:
            print(f"expenses database Error: {error}")
        finally:
            cursor.close()
            conn.close()

    def delete_expense_by_title(self, expense_title):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM expenses WHERE title = ?",(expense_title,))
            conn.commit()
            print("expenses deleted")
        except sqlite3.Error as error:
            print(f"expenses database Error: {error}")
        finally:
            cursor.close()
            conn.close()







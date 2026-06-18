"""
Pandas + Matplotlib charts
"""
import pandas as pd
import matplotlib.pyplot as plt
from database.connection import get_connection


def load_expenses_dataframe():
    conn = get_connection()

    try:
        query = """
                SELECT
                    id,
                    title,
                    category,
                    amount,
                    date,
                    payment_method
                FROM expenses \
                """

        df = pd.read_sql(query, conn)

        return df

    finally:
        conn.close()


def show_spending_by_category_bar_chart():
    df = load_expenses_dataframe()

    if df.empty:
        print("No expenses found. Add expenses before viewing analytics.")
        return

    category_totals = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(category_totals.index, category_totals.values)

    plt.title("Total Spending By Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")

    plt.tight_layout()
    plt.show()


def show_spending_by_payment_method_pie_chart():
    df = load_expenses_dataframe()

    if df.empty:
        print("No expenses found. Add expenses before viewing analytics.")
        return

    payment_totals = df.groupby("payment_method")["amount"].sum()

    plt.figure(figsize=(8, 5))

    plt.pie(
        payment_totals.values,
        labels=payment_totals.index,
        autopct="%1.1f%%"
    )

    plt.title("Spending By Payment Method")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    print("1. Spending By Category Bar Chart")
    print("2. Spending By Payment Method Pie Chart")

    choice = input("Choose chart: ")

    if choice == "1":
        show_spending_by_category_bar_chart()

    elif choice == "2":
        show_spending_by_payment_method_pie_chart()

    else:
        print("Invalid choice.")
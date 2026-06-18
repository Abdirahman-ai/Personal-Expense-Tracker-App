# CLI user interaction

from database.connection import setup
from models.expense import Expense
from services.expense_services import ExpenseService


def print_menu():
    print("\n======== Welcome to Expense Tracker Application ==========")
    print("1. Create Expense")
    print("2. Show All Expenses")
    print("3. Show Expense by ID")
    print("4. Show Expense by Title")
    print("5. Update Expense")
    print("6. Delete Expense by ID")
    print("7. Exit")


def main():
    setup()
    expense_service = ExpenseService()

    while True:
        print_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            title = input("Enter the title of the expense: ")
            amount = float(input("Enter the amount of the expense: "))
            category = input("Enter the category of the expense: ")
            date = input("Enter the date of the expense as YYYY-MM-DD: ")
            payment_method = input("Enter the payment method of the expense: ")

            expense = Expense(None, title, category, amount, date, payment_method)
            expense_service.add_expense(expense)

        elif choice == 2:
            all_expenses = expense_service.get_all_expenses()

            print("All expenses:")
            for expense in all_expenses:
                print(expense)

        elif choice == 3:
            expense_id = int(input("Enter the ID number of the expense: "))
            expense = expense_service.get_expense_by_id(expense_id)
            print(expense)

        elif choice == 4:
            expense_title = input("Enter the title of the expense: ")
            expense = expense_service.get_expense_by_title(expense_title)
            print(expense)

        elif choice == 5:
            expense_id = int(input("Enter the ID number of the expense to update: "))

            title = input("Enter the new title: ")
            amount = float(input("Enter the new amount: "))
            category = input("Enter the new category: ")
            date = input("Enter the new date as YYYY-MM-DD: ")
            payment_method = input("Enter the new payment method: ")

            updated_expense = Expense(None, title, category, amount, date, payment_method)
            expense_service.update_expense_by_id(expense_id, updated_expense)

        elif choice == 6:
            expense_id = int(input("Enter the ID number of the expense to delete: "))
            expense_service.delete_expense_by_id(expense_id)

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")


main()
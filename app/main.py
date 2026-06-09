# CLI user interaction

from database.connection import create_expenses_table
from models.expense import Expense
from repositories.expense_repository import ExpenseRepository
from services.expense_services import *

def print_menu():
    print("\n ======== Welcome to Expense Tracker Application ==========")
    print("1. Create Expense")
    print("2. Show All Expenses")
    print("3. Show Expense by id")
    print("4. Show Expense by title")
    print("5. Update Expense")
    print("6. Delete Expense")

print_menu()

expense_service = ExpenseService()
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # title, category, amount, date, payment_method
        print("Enter the title of the expense?: ")
        title = input()
        print("Enter the amount of the expense?: ")
        amount = float(input())
        print("Enter the category of the expense?: ")
        category = input()
        print("Enter the date of the expense as Date YYYY-MM-DD: ")
        date = input()
        print("Enter the payment method of the expense?: ")
        payment_method = input()

        # id, title, category, amount, date, payment_method
        expense = Expense(None, title, category, amount, date, payment_method)
        expense_service.add_expense(expense)
        break
    if choice == 2:
        all_expenses = expense_service.get_all_expenses()
        print("All the expenses:")
        for expense in all_expenses:
            print(expense)
        break
    if choice == 3:
        print("Enter the id number of the expense?: ")
        expense_id = input()
        print(expense_service.get_expense_by_id(expense_id))
        break
    if choice == 4:
        print("Enter the title of the expense?: ")
        expense_title = input()
        print(expense_service.get_expense_by_title(expense_title))
        break

# create_expenses_table()
# print("Expenses table created successfully.")
#
# repo = ExpenseRepository()
#
# expense1 = Expense(None,"Lunch","food",12.50,"2026-06-04","Debit Card")
# repo.add_expense(expense1)
#
# expense2 = Expense(None,"Dinner","food",20.50,"2026-06-04","Credit Card")
# repo.add_expense(expense2)
#
# expense3 = Expense(None,"Breakfast","food",8.50,"2026-06-04","Debit Card")
# repo.add_expense(expense3)
#
# # Getting all expenses
# all_expenses = repo.get_all_expenses()
# for exp in all_expenses:
#     print(exp)
#
# print("find by id: ", repo.get_expense_by_id(1))
#
# print("Find by title: ", repo.get_expense_by_title("Dinner"))
# # print("Found: ", repo.get_expense_by_id(2))
#
# print("DELETE BY ID: ", repo.delete_expense_by_id(1))
#
#
# print("UPDATE BY ID: ", repo.update_expense_by_id(19, Expense(None, "nothing", "nothing", 0.0, '2026-05-05', 'nothing')))
#
#
# print("find by id: ", repo.get_expense_by_id(19))
#
#
# print("DELETE BY TITLE: ", repo.delete_expense_by_title("Dinner"))
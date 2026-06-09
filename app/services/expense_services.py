""""
Business logic / validation
"""""
from models.expense import Expense
from repositories.expense_repository import ExpenseRepository

class ExpenseService:
    def __init__(self):
        self.expense_repository = ExpenseRepository()

    def add_expense(self, expense):
        if expense.amount <= 0:
            raise ValueError("Amount must be positive")
        self.expense_repository.add_expense(expense)


    def get_expense_by_id(self, expense_id: int):
        expense = self.expense_repository.get_expense_by_id(expense_id)

        if expense is None:
            print("Expense not found")
            return None
        return expense

    def get_expense_by_title(self, expense_title: str):
        expense = self.expense_repository.get_expense_by_title(expense_title)
        if expense is None:
            print(f"Expense not found by title {expense_title}")
            return None
        return expense

# delete_expense_by_id, update_expense_by_id, delete_expense_by_title
    def delete_expense_by_id(self, expense_id: int):
        expense = self.expense_repository.get_expense_by_id(expense_id)
        if expense is None:
            print("Expense not found")
            return None
        self.expense_repository.delete_expense_by_id(expense_id)
        return None

    def delete_expense_by_title(self, expense_title: str):
        expense = self.expense_repository.get_expense_by_title(expense_title)
        if expense is None:
            print("Expense not found")
            return None
        self.expense_repository.delete_expense_by_title(expense)
        return None

    def update_expense_id(self, expense_id, expense):
        expense = self.expense_repository.get_expense_by_id(expense_id)
        if expense is None:
            print("Expense not found")
            return None
        self.expense_repository.update_expense_by_id(expense_id, expense)
        return None

    def get_all_expenses(self):
        return self.expense_repository.get_all_expenses()


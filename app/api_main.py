from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from typing import List
from models.expense_api_model import (
    ExpenseApiModel,
    ExpenseResponseModel
)
from database.connection import setup
from models.expense import Expense
# from models.expense_api_model import ExpenseApiModel
from services.expense_services import ExpenseService

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

expense_service = ExpenseService()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}


@app.post("/expenses")
def create_expense(expense: ExpenseApiModel):

    expense_object = Expense(
        None,
        expense.title,
        expense.category,
        expense.amount,
        expense.date,
        expense.payment_method
    )

    expense_service.add_expense(expense_object)

    return {
        "message": f"Expense '{expense.title}' added successfully"
    }

@app.get("/expenses", response_model=List[ExpenseResponseModel])
def get_all_expenses():

    expenses = expense_service.get_all_expenses()

    response = []

    for expense in expenses:
        response.append(
            ExpenseResponseModel(
                id=expense.id,
                title=expense.title,
                category=expense.category,
                amount=expense.amount,
                date=str(expense.date),
                payment_method=expense.payment_method
            )
        )

    return response


@app.get("/expenses/{expense_id}", response_model=ExpenseResponseModel)
def get_expense_by_id(expense_id: int):

    expense = expense_service.get_expense_by_id(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return ExpenseResponseModel(
        id=expense.id,
        title=expense.title,
        category=expense.category,
        amount=expense.amount,
        date=str(expense.date),
        payment_method=expense.payment_method
    )

@app.get("/expenses/title/{expense_title}",
         response_model=ExpenseResponseModel)
def get_expense_by_title(expense_title: str):

    expense = expense_service.get_expense_by_title(expense_title)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return ExpenseResponseModel(
        id=expense.id,
        title=expense.title,
        category=expense.category,
        amount=expense.amount,
        date=str(expense.date),
        payment_method=expense.payment_method
    )

@app.put("/expenses/{expense_id}")
def update_expense(
        expense_id: int,
        expense: ExpenseApiModel
):

    updated_expense = Expense(
        None,
        expense.title,
        expense.category,
        expense.amount,
        expense.date,
        expense.payment_method
    )

    expense_service.update_expense_by_id(
        expense_id,
        updated_expense
    )

    return {
        "message": f"Expense {expense_id} updated successfully"
    }


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    expense = expense_service.get_expense_by_id(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    expense_service.delete_expense_by_id(expense_id)

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }

setup()

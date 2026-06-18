"""""
Pydantic model for FastAPI request/response validation.
"""""

from typing import Annotated
from pydantic import BaseModel, Field


class ExpenseApiModel(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    category: Annotated[str, Field(min_length=1, max_length=100)]
    amount: Annotated[float, Field(gt=0)]
    date: str
    payment_method: Annotated[str, Field(min_length=1, max_length=100)]



class ExpenseResponseModel(BaseModel):
    id: int
    title: str
    category: str
    amount: float
    date: str
    payment_method: str
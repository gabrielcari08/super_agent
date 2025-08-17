from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models.expenses import ExpenseCategory, PaymentMethod

#This is the schema for creating an expense
class ExpenseCreate(BaseModel):
    product: str
    amount: float
    category: ExpenseCategory
    payment_method: PaymentMethod
    date_of_expense: Optional[datetime] = None
    
#This is the schema for updating an expense
class ExpenseUpdate(BaseModel):
    product: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[ExpenseCategory] = None
    payment_method: Optional[PaymentMethod] = None
    date_of_expense: Optional[datetime] = None
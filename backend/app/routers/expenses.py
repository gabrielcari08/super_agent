from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependency import get_current_user, get_db
from app.models.expenses import Expense, PaymentMethod, ExpenseCategory
from app.models.user import User
from app.schemas.expenses import ExpenseCreate, ExpenseUpdate
from datetime import datetime

router = APIRouter(prefix="/expenses", tags=["Expenses"])

#Endpoint to create a new expense
@router.post("/add_expense")
async def create_expense(expense: ExpenseCreate,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    
    #Check if the product name is provided
    if not expense.product:
        raise HTTPException(status_code=400, detail="Product name is required")
    
    #Check if the amount is provided and is a positive number
    if expense.amount is None or expense.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be a positive number") 
    
    #Create the expense object
    new_expense = Expense(
        user_id=current_user.id,
        product=expense.product,
        amount=expense.amount,
        category=expense.category,
        payment_method=expense.payment_method,
        date_of_expense=expense.date_of_expense or datetime.utcnow()
    )
    
    #Add the expense to the database
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    
    return {"message": "Expense added successfully", "expense_id": new_expense.id}

#Endpoint to update an existing expense
@router.put("/update_expense/{expense_id}")
async def update_expense(expense_id: int,
                         expense_data: ExpenseUpdate,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    
    #Fetch the expense from the database
    #Equivalent to: SELECT * FROM expenses 
    #               WHERE id = expense_id AND user_id = [ID_CURRENT_USER]
    expense = db.query(Expense)\
        .filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
        
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    #Update the expense fields if provided
    if expense_data.product is not None:
        expense.product = expense_data.product
    if expense_data.amount is not None:
        if expense_data.amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be a positive number")
        expense.amount = expense_data.amount
    if expense_data.category is not None:
        expense.category = expense_data.category
    if expense_data.payment_method is not None:
        expense.payment_method = expense_data.payment_method
    if expense_data.date_of_expense is not None:
        expense.date_of_expense = expense_data.date_of_expense
    else:
        expense.date_of_expense = datetime.utcnow()
        
    #Commit the changes to the database
    db.commit()
    db.refresh(expense)
    
    return {"message": "Expense updated successfully", "expense_id": expense.id}

#Endpoint to delete an expense
@router.delete("/delete_expense/{expense_id}")
async def delete_expense(expense_id: int,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    
    #Fetch the expense from the database
    #Equivalent to: SELECT * FROM expenses 
    #               WHERE id = expense_id AND user_id = [ID_CURRENT_USER]
    expense = db.query(Expense)\
        .filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
        
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    #Delete the expense from the database
    db.delete(expense)
    db.commit()
    
    return {"message": "Expense deleted successfully", "expense_id": expense.id}

#Endpoint to get all expenses of the current user
@router.get("/get_expenses")
async def get_expenses(db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    
    #Fetch all expenses of the current user
    #Equivalent to: SELECT * FROM expenses WHERE user_id = [ID_CURRENT_USER]
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()
    
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")
    
    return [{"id": expense.id, "product": expense.product, "amount": expense.amount,
             "category": expense.category, "payment_method": expense.payment_method,
             "date_of_expense": expense.date_of_expense} for expense in expenses]
    
#Endpoint to get a specific expense by payment method
@router.get("/get_expense_by_payment_method")
async def get_expense_by_payment_method(payment_method: PaymentMethod,
                                        db: Session = Depends(get_db),
                                        current_user: User = Depends(get_current_user)):
    
    #Fetch expenses of the current user with the specified payment method
    #Equivalent to: SELECT * FROM expenses 
    #               WHERE user_id = [ID_CURRENT_USER] AND payment_method = payment_method
    expenses = db.query(Expense)\
        .filter(Expense.user_id == current_user.id,
                Expense.payment_method == payment_method)\
        .all()
        
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found for the specified payment method")
    
    return [{"id": expense.id, "product": expense.product, "amount": expense.amount,
             "category": expense.category, "payment_method": expense.payment_method,
             "date_of_expense": expense.date_of_expense} for expense in expenses]
    
#Endpoint to get a specific expense by category
@router.get("/get_expense_by_category")
async def get_expense_by_category(category: ExpenseCategory,
                                  db: Session = Depends(get_db),
                                  current_user: User = Depends(get_current_user)):
    
    #Fetch expenses of the current user with the specified category
    #Equivalent to: SELECT * FROM expenses 
    #               WHERE user_id = [ID_CURRENT_USER] AND category = category
    expenses = db.query(Expense)\
        .filter(Expense.user_id == current_user.id,
                Expense.category == category)\
        .all()
        
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found for the specified category")
    
    return [{"id": expense.id, "product": expense.product, "amount": expense.amount,
             "category": expense.category, "payment_method": expense.payment_method,
             "date_of_expense": expense.date_of_expense} for expense in expenses]
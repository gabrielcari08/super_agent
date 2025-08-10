from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import enum

class PaymentMethod(str, enum.Enum):
    cash = "Cash"
    transfer = "Transfer"
    
class ExpenseCategory(str, enum.Enum):
    food = "Food"
    school = "School"
    transport = "Transport"
    health = "Health"
    other = "Other"

#Modelos de gastos del usuario
class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    #Informacion del gasto
    product = Column(String (50))
    amount = Column(Integer)
    
    #Metodo de pago y categoria
    category = Column(Enum(ExpenseCategory), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    
    #Fecha del gasto
    date_of_expense = Column(DateTime, default=datetime.utcnow)
    
    #Relaciones
    user = relationship("User", back_populates="expenses")
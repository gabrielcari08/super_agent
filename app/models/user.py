from sqlalchemy import Column, Integer, String
from app.core.database import Base

#Modelo de usuario
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String (20))
    surname = Column(String (20))
    hashed_password = Column(String, nullable=False)
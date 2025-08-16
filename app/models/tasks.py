from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import enum

class TaskType(str, enum.Enum):
    homework = "Homework"
    practical_work = "Practical Work"
    test = "Test"
    
class TaskPriority(str, enum.Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class TaskStatus(str, enum.Enum):
    pending = "Pending"
    in_progress = "In Progress"
    finished = "Finished"
    cancelled = "Cancelled"
    
class SubjectType(str, enum.Enum):
    math = "Math"
    chemistry = "Chemistry"
    physics = "Physics"
    language_and_literature = "Language and Literature"
    history = "History"
    philosophy = "Philosophy"
    social_sciences_workshop = "Social Sciences Workshop"
    programming = "Programming"
    robotics = "Robotics"
    english = "English"
    physical_education = "Physical Education"
    
#Modelo de tareas del usuario
class Task(Base):
    
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    #Informacion Basica de la tarea
    title = Column(String(100), nullable=False)  
    subject = Column(String(60), nullable=False, index=True)
    task_type = Column(Enum(TaskType), nullable=False)
    description = Column(Text) 
    
    #Fechas y tiempo 
    date_of_task = Column(DateTime, default=datetime.utcnow) #<- Fecha en la que te estan dando la tarea
    date_of_presentation = Column(DateTime) #<- Fecha en la que se debe presentar 
    
    #Estado y prioridad
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, nullable=False)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium, nullable=False)
    
    #Relaciones
    user = relationship("User", back_populates="tasks")
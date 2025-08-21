from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.tasks import TaskType, TaskStatus, TaskPriority, SubjectType

#This class defines the structure for tasks creation.
class TaskCreate(BaseModel):
    title: str
    subject: SubjectType 
    task_type: TaskType
    description: str
    date_of_task: Optional[datetime] = None
    date_of_presenation: datetime
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    
#This class defines the structure for tasks update.
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    subject: Optional[SubjectType] = None
    task_type: Optional[TaskType] = None
    description: Optional[str] = None
    date_of_task: Optional[datetime] = None
    date_of_presenation: Optional[datetime] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    

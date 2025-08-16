from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependency import get_current_user, get_db
from app.schemas.tasks import TaskCreate, TaskUpdate
from app.models.tasks import Task
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Endpoint for create a new task.
@router.post("/create_task")
async def create_task(task_data: TaskCreate,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    
    # Check if the user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Validate the task data
    if not task_data.title:
        raise HTTPException(status_code=400, detail="Missing required field: title")
    
    # Check if the task have a description
    if not task_data.description:
        raise HTTPException(status_code=400, detail="Description is required")
    
    # Check if the task have a date of presentation
    if task_data.date_of_presenation is None:
        raise HTTPException(status_code=400, detail="Presentation date is required")
    
    # Create the task instance
    task = Task(
        user_id=current_user.id,
        title=task_data.title,
        subject=task_data.subject,
        task_type=task_data.task_type,
        description=task_data.description,
        date_of_task=task_data.date_of_task,
        date_of_presentation=task_data.date_of_presenation,
        status=task_data.status,
        priority=task_data.priority
    )
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {"message": "Task created successfully", "task_id": task.id}
    


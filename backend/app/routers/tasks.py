from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependency import get_current_user, get_db
from app.schemas.tasks import TaskCreate, TaskUpdate
from app.models.tasks import Task, TaskType, TaskStatus, TaskPriority, SubjectType
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Endpoint for create a new task.
@router.post("/create_task")
async def create_task(task_data: TaskCreate,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    
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


#Endpoint for update an existing task.
@router.put("/update_task/{task_id}")
async def update_task(task_id: int,
                      task_data: TaskUpdate,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    
    # Fetch the task from the database
    # Equivalent to: SELECT * FROM tasks WHERE id = task_id AND user_id = [ID_CURRRENT_USER] LIMIT 1
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update the task fields
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.subject is not None:
        task.subject = task_data.subject
    if task_data.task_type is not None:
        task.task_type = task_data.task_type
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.date_of_task is not None:
        task.date_of_task = task_data.date_of_task
    if task_data.date_of_presenation is not None:
        task.date_of_presentation = task_data.date_of_presenation
    if task_data.status is not None:
        task.status = task_data.status
    if task_data.priority is not None:
        task.priority = task_data.priority
        
    db.commit()
    db.refresh(task)
    
    return {"message": "Task updated successfully", "task_id": task.id}

#Endpoint for delete an existing task.
@router.delete("/delete_task/{task_id}")
async def delete_task(task_id: int,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):

    # Fetch the task from the database
    # Equivalent to: SELECT * FROM tasks WHERE id = task_id AND user_id = [ID_CURRRENT_USER]
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Delete the task
    db.delete(task)
    db.commit()
    
    return {"message": "Task deleted successfully", "task_id": task.id}

#Endpoint for get all tasks of the current user.
@router.get("/get_tasks")
async def get_tasks(db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):

    # Fetch all tasks for the current user
    # Equivalent to: SELECT * FROM tasks WHERE user_id = [ID_CURRRENT_USER]
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    
    return [{"id": task.id, "title": task.title, "subject": task.subject, "task_type": task.task_type,
             "description": task.description, "date_of_task": task.date_of_task,
             "date_of_presentation": task.date_of_presentation, "status": task.status,
             "priority": task.priority} for task in tasks]
    
#Endpoint for get a specific task by subject.
@router.get("/get_tasks_of_subject")
async def get_task(subject: SubjectType,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    # Fetch the task by subject for the current user
    # Equivalent to: SELECT * FROM tasks WHERE subject = subject AND user_id = [ID_CURRRENT_USER]
    tasks = db.query(Task).filter(Task.subject == subject, Task.user_id == current_user.id).all()
    
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    
    return [{"id": task.id, "title": task.title, "subject": task.subject, "task_type": task.task_type,
             "description": task.description, "date_of_task": task.date_of_task,
             "date_of_presentation": task.date_of_presentation, "status": task.status,
             "priority": task.priority} for task in tasks]

#Endpoint for get a specific task by task type.
@router.get("/get_tasks_of_type")
async def get_task(task_type: TaskType,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    # Fetch the task by type for the current user
    # Equivalent to: SELECT * FROM tasks WHERE task_type = task_type AND user_id = [ID_CURRRENT_USER]
    tasks = db.query(Task).filter(Task.task_type == task_type, Task.user_id == current_user.id).all()
    
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    
    return [{"id": task.id, "title": task.title, "subject": task.subject, "task_type": task.task_type,
             "description": task.description, "date_of_task": task.date_of_task,
             "date_of_presentation": task.date_of_presentation, "status": task.status,
             "priority": task.priority} for task in tasks]
    
#Endpoint for get a specific task by status.
@router.get("/get_tasks_of_status")
async def get_task(status: TaskStatus,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    # Fetch the task by status for the current user
    # Equivalent to: SELECT * FROM tasks WHERE status = status AND user_id = [ID_CURRRENT_USER]
    tasks = db.query(Task).filter(Task.status == status, Task.user_id == current_user.id).all()
    
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    
    return [{"id": task.id, "title": task.title, "subject": task.subject, "task_type": task.task_type,
             "description": task.description, "date_of_task": task.date_of_task,
             "date_of_presentation": task.date_of_presentation, "status": task.status,
             "priority": task.priority} for task in tasks]
    
#Endpoint for get a specific task by priority.
@router.get("/get_tasks_of_priority")
async def get_task(priority: TaskPriority,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    # Fetch the task by priority for the current user
    # Equivalent to: SELECT * FROM tasks WHERE priority = priority AND user_id = [ID_CURRRENT_USER]
    tasks = db.query(Task).filter(Task.priority == priority, Task.user_id == current_user.id).all()
    
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    
    return [{"id": task.id, "title": task.title, "subject": task.subject, "task_type": task.task_type,
             "description": task.description, "date_of_task": task.date_of_task,
             "date_of_presentation": task.date_of_presentation, "status": task.status,
             "priority": task.priority} for task in tasks]
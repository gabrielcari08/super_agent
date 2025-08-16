from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependency import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.hashing import Hash

router = APIRouter(prefix="/users", tags=["Users"])

#Endpoint for user registration.
@router.post("/create_user")
async def create_user(user: UserCreate,
                      db: Session = Depends(get_db)):
    
    #Search database if user already exists.
    #Equivalent to: SELECT * FROM users 
    #               WHERE users.name = [user.name] 
    #               AND users.username = [user.surname] 
    #               LIMIT 1;
    user_exists = db.query(User).filter(User.name == user.name,
                                        User.surname == user.surname)\
                                .first()
                                
    #If user already exists throw an excepcion.
    if user_exists:
        raise HTTPException(status_code=400,
                            detail="The user already exists")
        
    #Password hash.
    hashed_password = Hash.bcrypt(user.password)
    
    #Create a new instance for User
    new_user = User(
        name = user.name,
        surname = user.surname,
        hashed_password = hashed_password
    )
    
    #Save this instance in the database.
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "¡The user was created succesfully!"}
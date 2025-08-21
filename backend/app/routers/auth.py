from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependency import get_db
from app.auth.jwt_handler import create_access_token
from app.auth.hashing import Hash
from app.models.user import User
from app.schemas.user import UserLogin, Token

router = APIRouter(prefix="/auth", tags=["Auth"])

#Endpoint for the user login. 
@router.post("/login", response_model=Token)
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    #Search in database if the user name and surname matches with the one entered.
    #Equivalent to: SELECT * FROM users 
    #               WHERE user.name = [user_credentials.name] 
    #               AND user.username = [user_credential.surname] 
    #               LIMIT 1;
    user = db.query(User).filter(User.name == user_credentials.name,
                                 User.surname == user_credentials.surname).first()
    
    #If the user doesnt exists or the credentials are incorrect throw an exception.
    if not user:
        raise HTTPException(status_code=401,
                            detail="Credenciales incorrectas"
        )
        
    #Verify that the entered password matches with the save and hashed password.
    if not Hash.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401,
                            detail="Credenciales incorrectas"
        )
    
    #If all is correct, generate the token with the user id.
    access_token = create_access_token(user_id=user.id) #Antes: data={"user_id": user.id} 
    
    #Return token JWT
    return {"access_token": access_token, "token_type": "bearer"}
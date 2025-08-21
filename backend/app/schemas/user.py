from pydantic import BaseModel

#This class defined the estructure to user creation
class UserCreate(BaseModel):
    name: str
    surname: str
    password: str

#This class defined the estructure to user login
class UserLogin(BaseModel):
    name: str
    surname: str
    password: str

#This class difined the token response    
class Token(BaseModel):
    access_token: str
    token_type: str


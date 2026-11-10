from datetime import datetime
from pydantic import BaseModel,EmailStr,ConfigDict,Field

class UserRead(BaseModel):
    id:int
    email:EmailStr
    role:str
    is_active:bool
    created_at:datetime

    model_config=ConfigDict(from_attributes=True) # lets Pydantic read SQLAlchemy objects

class CreateUser(BaseModel):
    email:EmailStr
    password:str=Field(max_length=256,min_length=8)

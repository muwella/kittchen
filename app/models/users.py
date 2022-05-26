#Pydantic
from pydantic import BaseModel, EmailStr, Field


# models

class UserBase(BaseModel):
    username: str = Field(min_length=1,max_length=50,example='muwella')
    nickname: str = Field(min_length=1,max_length=50,example='Maru')
    email: EmailStr


class UserIn(UserBase):
    password: str


# WIP hashed password
class UserInDB(UserBase):
    hashed_password: str


class UserOut(UserBase):
    pass
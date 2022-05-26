#Pydantic
from pydantic import BaseModel, EmailStr, Field


# models

class UserBase(BaseModel):
    username: str = Field(min_length=1,max_length=50,example='muwella')
    nickname: str = Field(min_length=1,max_length=50,example='Maru')
    email: EmailStr


# WIP hash password (security)
class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


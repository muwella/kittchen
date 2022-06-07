from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from ..schemas.recipes import RecipeInResponse

# pydantic models

class UserInLogin(BaseModel):
    email: EmailStr
    password: str


class UserBase(BaseModel):
    username: str = Field(min_length=1,max_length=50,example='muwella')
    nickname: str = Field(min_length=1,max_length=50,example='Maru')
    email: EmailStr


class UserInCreate(UserBase):
    password: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class UserInResponse(UserBase):
    token: str
    recipes: list[RecipeInResponse] = []

    class Config:
        orm_mode = True
        # schema_extra = {}


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None




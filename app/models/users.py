#Pydantic
from pydantic import BaseModel, Field


# models

# LOOKUP pydantic EmailStr
class UserBase(BaseModel):
    nickname: str = Field(
        min_length=1,
        max_length=50,
        example='Maru'
    )
    username: str = Field(
        min_length=1,
        max_length=50,
        example='muwella'
    )
    email: str = Field(
        regex=r"^[a-zA-Z0-9_.+-ñÑ]+@[a-zA-Z0-9-ñÑ]+\.[a-zA-Z0-9-.ñÑ]+$"
    )


# WIP hash password (security)
class User(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInLogin():
    pass


class UserInCreate():
    pass
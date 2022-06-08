from typing import Union

from pydantic import BaseModel, EmailStr, Field

from ..schemas.recipes import RecipeInResponse

# pydantic models

# received from user
class UserBase(BaseModel):
    username: str
    nickname: str
    email: EmailStr

    class Config:
        schema_extra = {
            'example': {
                'username': 'muwella',
                'nickname': 'Maru',
                'email': 'marielabrascon@gmail.com'
            }
        }


# sent to user
class User(UserBase):
    id: int
    is_active: bool
    recipes: list[RecipeInResponse] = []

    class Config:
        # orm_mode is to make the Pydantic model compatible
            # with ORMs and I can declare it in the
            # response_model argument in path operations
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'muwella',
                'nickname': 'Maru',
                'email': 'marielabrascon@gmail.com'
            }
        }


class UserInCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'muwella',
                'nickname': 'Maru',
                'email': 'marielabrascon@gmail.com',
                'password': 'bigTime'
            }
        }


class UserInResponse(User):
    pass


class UserInUpdate(BaseModel):
    username: Union[str, None] = Field(default=None)
    nickname: Union[str, None] = Field(default=None)
    email: Union[EmailStr, None] = Field(default=None)
    password: Union[str, None] = Field(default=None)


class UserInLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'marielabrascon@gmail.com',
                'password': 'landOfConfusion'
            }
        }



from typing import Union

from pydantic import BaseModel, EmailStr, Field

from ..schemas.recipes import RecipeInResponse

# pydantic models

# received from user
class UserBase(BaseModel):
    email: str
    nickname: str

    class Config:
        schema_extra = {
            'example': {
                'nickname': 'Maru',
                'email': 'marielabrascon@gmail.com'
            }
        }


# sent to user
# in the Pydantic model for reading, add orm_mode = True
class User(UserBase):
    id: int
    is_active: bool
    # recipes: list[RecipeInResponse] = []

    class Config:
        # orm_mode is to make the Pydantic model compatible
            # with ORMs and I can declare it in the
            # response_model argument in path operations
        orm_mode = True
        schema_extra = {
            'example': {
                'nickname': 'Maru',
                'email': 'marielabrascon@gmail.com',
                'id': 1,
                'is_active': True
            }
        }


class UserInCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'marielabrascon@gmail.com',
                'nickname': 'Maru',
                'password': 'bigTime'
            }
        }


class UserInResponse(User):
    pass


class UserInUpdate(BaseModel):
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



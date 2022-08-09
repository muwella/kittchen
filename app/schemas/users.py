from typing import Union
from pydantic import BaseModel, Field

# pydantic models

class UserBase(BaseModel):
    username: str
    email: str
    nickname: str

    class Config:
        schema_extra = {
            'example': {
                'nickname': 'Maru',
                'username': 'muwella',
                'email': 'marielabrascon@gmail.com'
            }
        }


# sent to user
    # this scheme has DB added info
class User(UserBase):
    id: int
    is_active: bool

    # in the Pydantic model for reading, add orm_mode = True
        # this is because orm_mode makes the Pydantic model
        # compatible with ORMs and I can declare it in the
        # response_model argument in path operations
    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'muwella',
                'email': 'marielabrascon@gmail.com',
                'nickname': 'Maru',
                'id': 1,
                'is_active': True
            }
        }


# received from user
class UserInCreate(UserBase):
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'muwella',
                'email': 'marielabrascon@gmail.com',
                'nickname': 'Maru',
                'password': 'bigTime'
            }
        }


class UserInResponse(User):
    pass


# received from user
class UserInUpdate(BaseModel):
    nickname: Union[str, None] = Field(default=None)
    password: Union[str, None] = Field(default=None)


# received from user
class UserInLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'muwella',
                'password': 'bigTime'
            }
        }



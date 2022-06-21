#Python
from typing import Union
#Pydantic
from pydantic import BaseModel, Field

# received from user

class RecipeCategoryBase(BaseModel):
    name: str


class RecipeCategoryInCreate(RecipeCategoryBase):
    pass


class RecipeCategoryInUpdate(BaseModel):
    name: Union[str, None] = Field(default=None)


# sent to user

class RecipeCategory(RecipeCategoryBase):
    id: int
    is_default: bool

    class Config:
        orm_mode = True
        schema_extra = {
            'example default': {
                'name': 'meal',
                'id': 1,
                'is_default': True
            },
            'example': {
                'name': 'party food',
                'id': 3,
                'is_default': False
            }
        }


class RecipeCategoryInResponse(RecipeCategory):
    pass

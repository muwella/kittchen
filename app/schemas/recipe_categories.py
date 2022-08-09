from typing import Union
from pydantic import BaseModel, Field

# pydantic models

class RecipeCategoryBase(BaseModel):
    name: str

    class Config:
        schema_extra = {
            'example': {
                'name': 'Birthdays'
            }
        }


# sent to user
    # this scheme has DB added info
class RecipeCategory(RecipeCategoryBase):
    id: int
    is_default: bool

    # in the Pydantic model for reading, add orm_mode = True
        # this is because orm_mode makes the Pydantic model
        # compatible with ORMs and I can declare it in the
        # response_model argument in path operations
    class Config:
        orm_mode = True
        schema_extra = {
            'example default': {
                'id': 1,
                'name': 'Meals',
                'is_default': True
            },
            'example': {
                'id': 3,
                'name': 'Birthdays',
                'is_default': False
            }
        }


# received from user
class RecipeCategoryInCreate(RecipeCategoryBase):
    pass


class RecipeCategoryInResponse(RecipeCategory):
    pass


# received from user
class RecipeCategoryInUpdate(BaseModel):
    name: Union[str, None] = Field(default=None)


from typing import Union
from pydantic import BaseModel, Field

# pydantic models

class IngredientBase(BaseModel):
    name: str
    # category_id: int

    class Config:
        schema_extra = {
            'example': {
                'name': 'Tomato',
                'category_id': 1
            }
        }


# sent to user
    # this scheme has DB added info
class Ingredient(IngredientBase):
    id: int

    # in the Pydantic model for reading, add orm_mode = True
        # this is because orm_mode makes the Pydantic model
        # compatible with ORMs and I can declare it in the
        # response_model argument in path operations
    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'id': 10,
                'name': 'Tomato',
                'category_id': 1
            }
        }


# received from user
class IngredientInCreate(IngredientBase):
    pass


class IngredientInResponse(Ingredient):
    pass


# received from user
class IngredientInUpdate(BaseModel):
    name: Union[str, None] = Field(default=None)
    # category_id: Union[int, None] = Field(default=None)
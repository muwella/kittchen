from typing import Union
from pydantic import BaseModel, Field

# pydantic models

class IngredientBase(BaseModel):
    name: str
    category_id: int

    class Config:
        schema_extra = {
            'example': {
                'name': 'Tomato',
                'category_id': 1
            }
        }


# sent to user
    # this scheme has DB added info
# TBD add is_default? add other things? DEFINE
class Ingredient(IngredientBase):
    id: int

    class Config:
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
    category_id: Union[int, None] = Field(default=None)
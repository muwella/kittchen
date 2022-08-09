#Python
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field


class IngredientCategory(Enum):
    pass
#     cereals = 0
#     fruits = 1
#     vegetables = 2
#     dairy = 3
#     meat = 4
#     fats = 5


class IngredientBase(BaseModel):
    name: str
    category_id: int




class Ingredient(BaseModel):
    pass
#     name: str = Field(
#         min_length=1,
#         max_length=50,
#         example='banana'
#     )
#     category: IngredientCategory = Field(
#         default=None,
#         example='fruit'
#     )


# received from user
class IngredientInCreate(IngredientBase):
    pass
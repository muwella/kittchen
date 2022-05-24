#Python
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field


# LOOKUP should i use enum with int or str
class IngredientCategory(Enum):
    cereals = 0
    fruits = 1
    vegetables = 2
    dairy = 3
    meat = 4
    fats = 5


class Ingredient(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example='banana'
    )
    category: IngredientCategory = Field(
        default=None,
        example='fruit'
    )


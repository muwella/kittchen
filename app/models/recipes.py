#Python
from typing import Union, List
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field


# LOOKUP could every user add elements to their own enum?
    # i don't think so
class RecipeCategory(str, Enum):
    meal = 'meal'
    dessert = 'dessert'


# TBD tags, likes, comments
# TBD modify recipes of others?
class Recipe(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example="Noodles"
    )
    # list of ingriedients IDs
    ingredients: List[int] = Field(
        example=[1,2,3]
    )
    steps: Union[str, None] = Field(
        default=None,
        example="Boil, eat, repeat"
    )
    category: Union[RecipeCategory, None] = Field(
        default=None,
        example="meal"
    )


#Python
from typing import Union
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

# LOOKUP ingredients = list[Ingredient.id] ? smth like that
    # or look up the int in DB and check if there's an ingredient with that ID
    # maybe i'll be able to connect them when i see DB management
class Recipe(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    ingredients: list[int] = set()
    steps: Union[str, None] = Field(default=None)
    category: Union[RecipeCategory, None] = Field(default=None)

    # LOOKUP using schema_extra to add metatada for a frontend user interface
    class Config:
        schema_extra = {
            "example": {
                # "token": token,
                "name": "Noodles",
                "ingredients": [1, 2, 3],
                "steps": "Boil, eat, repeat",
                "category": "meal"
            }
        }


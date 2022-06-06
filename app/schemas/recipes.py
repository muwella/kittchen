#Python
from typing import Union
#Pydantic
from pydantic import BaseModel, Field



class RecipeCategoryOut(BaseModel):
    pass

# WIP add meal and dessert to RecipeCategory

# TBD tags, likes, comments



# LOOKUP ingredients = list[Ingredient.id] ? smth like that
    # or look up the int in DB and check if there's an ingredient with that ID
    # maybe i'll be able to connect them when i see DB management
class RecipeOut(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    ingredients: list[int] = set()
    steps: Union[str, None] = Field(default=None)
    category: Union[RecipeCategoryOut, None] = Field(default=None)

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


#Python
from typing import Union
#Pydantic
from pydantic import BaseModel, Field


# received from user

class RecipeBase(BaseModel):
    name: str
    steps: Union[str, None] = Field(default=None)
    category: str        


class RecipeInCreate(RecipeBase):
    pass


# TBD ingredients
class RecipeInUpdate(RecipeBase):
    name: Union[str, None] = Field(default=None)
    ingredients: Union[list[int], None] = Field(default=None)
    steps: Union[str, None] = Field(default=None)
    category: Union[str, None] = Field(default=None)


# sent to user

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Noodles",
                "ingredients": [1, 2, 3],
                "steps": "Boil, eat, repeat",
                "category": "meal",
                "id": 7
            }
        }


class RecipeInResponse(Recipe):
    pass
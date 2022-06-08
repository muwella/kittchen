#Python
from enum import Enum
from typing import Union
#Pydantic
from pydantic import BaseModel, Field

# WIP add meal and dessert to RecipeCategory

# received from user
class RecipeCategoryBase(Enum):
    name: str


# sent to user
class RecipeCategory(RecipeCategoryBase):
    id: int

    class Config:
        orm_mode = True


# received from user
class RecipeBase(BaseModel):
    name: str
    steps: Union[str, None] = Field(default=None)
    category: RecipeCategoryBase

    class Config:
        schema_extra = {
            "example": {
                "name": "Noodles",
                "ingredients": [1, 2, 3],
                "steps": "Boil, eat, repeat",
                "category": "0"
            }
        }


# sent to user
class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True


class RecipeInCreate(RecipeBase):
    pass


class RecipeInResponse(Recipe):
    pass


class RecipeInUpdate(RecipeBase):
    name: Union[str, None] = Field(default=None)
    ingredients: Union[list[int], None] = Field(default=None)
    steps: Union[str, None] = Field(default=None)
    category: Union[RecipeCategoryBase, None] = Field(default=None)
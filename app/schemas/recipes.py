#Python
from typing import Union
#Pydantic
from pydantic import BaseModel, Field

# WIP add meal and dessert to RecipeCategory
# TBD tags, likes, comments


class RecipeCategoryInResponse(BaseModel):
    pass


class RecipeBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    ingredients: list[int] = set()
    steps: Union[str, None] = Field(default=None)
    category: Union[RecipeCategoryInResponse, None] = Field(default=None)

    # LOOKUP using schema_extra to add metatada for a frontend user interface
    class Config:
        orm_mode = True
        # schema_extra = {
        #     "example": {
        #         # "token": token,
        #         "name": "Noodles",
        #         "ingredients": [1, 2, 3],
        #         "steps": "Boil, eat, repeat",
        #         "category": "meal"
        #     }
        # }


class RecipeInCreate(RecipeBase):
    pass


class RecipeInResponse(BaseModel):
    pass


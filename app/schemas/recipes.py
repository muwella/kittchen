from typing import Union
from pydantic import BaseModel, Field

# pydantic models

# NOTE ingredients are not saved on the same table as recipes
class RecipeBase(BaseModel):
    name: str
    steps: Union[str, None] = Field(default=None)
    category_id: Union[int, None] = Field(default=None)
    ingredients_id: Union[list[int], None] = Field(default=None)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Noodles',
                'steps': 'Boil, eat, repeat',
                'category_id': None,
                'ingredients_id': [1, 2, 3, 6, 12]
            }
        }


# sent to user
    # this scheme has DB added info
class Recipe(RecipeBase):
    id: int

    # in the Pydantic model for reading, add orm_mode = True
        # this is because orm_mode makes the Pydantic model
        # compatible with ORMs and I can declare it in the
        # response_model argument in path operations
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Noodles",
                "steps": "Boil, eat, repeat",
                "category_id": 1,
                "ingredients_id": [1, 2, 3, 6, 12],
                "id": 7
            }
        }


# received from user
class RecipeInCreate(RecipeBase):
    pass


class RecipeInResponse(Recipe):
    pass


# received from user
class RecipeInUpdate(BaseModel):
    name: Union[str, None] = Field(default=None)
    steps: Union[str, None] = Field(default=None)
    category_id: Union[str, None] = Field(default=None)
    ingredients_id: Union[list[int], None] = Field(default=None)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Noodles with sauce',
                'steps': 'Boil, add sauce, eat, repeat',
                'category_id': 1,
                'ingredients_id': [1, 2, 3, 6, 12, 15]
            }
        }

# Pydantic
from pydantic import BaseModel

# pydantic models

# sent to user
class IngredientCategory(BaseModel):
    name: str
    id: int

    # in the Pydantic model for reading, add orm_mode = True
        # this is because orm_mode makes the Pydantic model
        # compatible with ORMs and I can declare it in the
        # response_model argument in path operations
    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'name': 'Fruits',
                'id': 1
            }
        }


class IngredientCategoryInResponse(IngredientCategory):
    pass
# python
from typing import Union
# SQLAlchemy
from sqlalchemy.orm import Session
# models (DB) & schemas
from ..schemas.ingredients import IngredientInCreate
from ..models.recipes import IngredientInDB

# create

def create_ingredient(
    ingredient: IngredientInCreate,
    db: Session
):
    ingredient_in_db = IngredientInDB(
        **ingredient.dict()
    )


# read

def get_ingredient_by_id(
    id: int,
    db: Session
) -> Union[IngredientInDB, None]:
    return db.query(IngredientInDB).filter(IngredientInDB.id == id).first()


# update


# delete
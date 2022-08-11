# python
from typing import Union
# SQLAlchemy
from sqlalchemy.orm import Session
# models (DB) & schemas
from ..schemas.ingredients import IngredientInCreate, IngredientInResponse, IngredientInUpdate
from ..models.recipes import IngredientInDB

# DOUBT why refresh?

# create

def create_ingredient(
    ingredient: IngredientInCreate,
    user_id: int,
    db: Session
):
    # create ingredient instance
    ingredient_in_db = IngredientInDB(
        **ingredient.dict()
    )

    db.add(ingredient_in_db)
    db.commit()
    db.refresh(ingredient_in_db)

    return {'ingredient': ingredient_in_db}


# read

def get_ingredient_by_id(id: int, db: Session) -> Union[IngredientInDB, None]:
    return db.query(IngredientInDB).filter(IngredientInDB.id == id).first()


def get_ingredient_by_name(name: str, user_id: int, db: Session) -> Union[IngredientInDB, None]:
    return db.query(IngredientInDB).filter(
        IngredientInDB.creator_id == user_id 
        and IngredientInDB.name == name
        ).first()


# update

def update_ingredient(ingredient_update: IngredientInUpdate, ingredient_in_db: IngredientInDB, db: Session):
    if ingredient_update.name:
        ingredient_in_db.name = ingredient_update.name

    db.commit()
 
    return get_ingredient_by_id(ingredient_in_db.id, db)


# delete

def delete_ingredient(ingredient: IngredientInDB, db: Session):
    db.delete(ingredient)
    db.commit()

# SQLAlchemy
from sqlalchemy.orm import Session
# models
from ..models.recipes import RecipeInDB
from ..schemas.recipes import RecipeInCreate


def get_recipe_by_id(db: Session, recipe_id: id):
    return db.query(RecipeInDB).filter(RecipeInDB.id == recipe_id).first()


def get_recipe_by_name(db: Session, recipe_name: str, owner_id: id):
    return db.query(RecipeInDB).filter(RecipeInDB.name == recipe_name).first()


def create_recipe(
    db: Session,
    recipe: RecipeInCreate,
    ingredients: list[int],
    user_id = int
    ):
    # WIP a recipe-ingredient relationship table
    
    db_recipe = RecipeInDB(**recipe.dict(), creator_id = user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # if the user can send an int on the list,
    # that ingredient has to exist on the DB, otherwise
    # raise an error

    for i in ingredients:
        # db.query(IngredientInDB).filter(IngredientInDB.id == i).first()
        # add a recipe-ingredient relationship with each id
        pass

    return db_recipe

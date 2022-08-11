# FastAPI
from fastapi import HTTPException
# python
from typing import Union
# SQLAlchemy
from sqlalchemy.orm import Session
# models (DB) & schemas
from ..models.recipes import IngredientInDB, RecipeInDB
from ..schemas.recipes import RecipeInCreate
# utils
from ..utils.ingredients import get_ingredient_by_id


# create

def create_recipe(
    recipe: RecipeInCreate,
    user_id: int,
    db: Session
):
    # create recipe instance
    recipe_in_db = RecipeInDB(
        **recipe.dict(exclude={'ingredients_id'})
    )

    db.add(recipe_in_db)

    # create relationships between recipe and ingredients
    for i in recipe.ingredients_id:
        # look for ingredient in db
        ingredient_in_db = get_ingredient_by_id(i, db)
        recipe.ingredients.append(ingredient_in_db)

    db.commit()

    return {'recipe': recipe_in_db}


# read

def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(RecipeInDB).filter(RecipeInDB.id == recipe_id).first()


# don't think i'll use it
def get_recipe_by_name(db: Session, recipe_name: str, user_id: id):
    user_recipes = db.query(RecipeInDB).filter(RecipeInDB.creator_id == user_id)
    return user_recipes.filter(RecipeInDB.name == recipe_name).first()


# filter


def filter_recipes_by_category(db: Session, category_id: int):
    return db.query(RecipeInDB).filter(RecipeInDB.category_id == category_id)


# returns every recipe that contains string in it's name
    # example: string 'oli' would return 'ravioli' and 'alioli sauce'
def filter_recipes_by_string(string: str, db: Session):
    return db.query(RecipeInDB).filter(string in RecipeInDB.name)


# update


# delete




# WIP to create recipes, ingredients and their relationships!!

 # Rows in RecipeInDB and IngredientInDB get created as normal
        # recipe = RecipeInDB(...)
        # ingredient1 = IngredientInDB(...)
        # db.session.add_all([recipe, ingredient1])
        # db.session.commit()
    
    # Then
        # recipe.ingredients.append(ingredient1)
        # db.session.commit()

    # to remove item:
        # recipe.ingredients.remove(ingredient1)
        # db.session.commit()
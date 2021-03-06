# SQLAlchemy
from sqlalchemy.orm import Session
# models
from ..models.recipes import RecipeInDB
from ..schemas.recipes import RecipeInCreate
from ..utils.recipe_categories import get_category_by_string


# WIP raise exceptions
    # recipe doesn't exist
    # category doesn't exist


def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(RecipeInDB).filter(RecipeInDB.id == recipe_id).first()


# DOUBT can i send this query as a JSON?
def filter_recipes_by_category(db: Session, category_id: int):
    return db.query(RecipeInDB).filter(RecipeInDB.category_id == category_id)


# returns every recipe that contains string in it's name
    # example: string 'oli' would return 'ravioli' and 'alioli sauce'
def filter_recipes_by_string(string: str, db: Session):
    return db.query(RecipeInDB).filter(string in RecipeInDB.name)


# don't think i'll use it
def get_recipe_by_name(db: Session, recipe_name: str, user_id: id):
    user_recipes = db.query(RecipeInDB).filter(RecipeInDB.creator_id == user_id)
    return user_recipes.filter(RecipeInDB.name == recipe_name).first()


def create_recipe(
    db: Session,
    recipe: RecipeInCreate,
    ingredients_id: list[int],
    user_id = int
    ):

    # get category_id from string received
    category = get_category_by_string(db, recipe.category)

    # get ingredients IDs from list[int] received
    for id in ingredients_id:
        # db.query(IngredientInDB).filter(IngredientInDB.id == id).first()
        # add a recipe-ingredient relationship with each id
        pass

    recipe_in_db = RecipeInDB(
        **recipe.dict(exclude={'category'}),
        category_id=1,
        creator_id = user_id
    )
    
    db.add(recipe_in_db)
    db.commit()
    db.refresh(recipe_in_db)

    return {'recipe in db': recipe_in_db}

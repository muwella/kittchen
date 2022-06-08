# SQLAlchemy
from sqlalchemy.orm import Session
# models
from ..models.users import UserInDB
from ..schemas.users import UserInResponse, UserInCreate
from ..models.recipes import RecipeInDB, RecipeCategory
from ..schemas.recipes import RecipeInResponse, RecipeInCreate
from ..models.ingredients import IngredientInDB


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserInDB).filter(UserInDB.email == email).first()


def create_user(db: Session, user: UserInCreate):
    hashed_password = user.password # WIP
    db_user = UserInDB(
        username = user.username,
        nickname = user.nickname,
        email = user.email,
        hashed_password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_recipe(db: Session, recipe_id: id):
    return db.query(RecipeInDB).filter(RecipeInDB.id == recipe_id).first()


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

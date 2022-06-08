from sqlalchemy.orm import Session

from ..models.users import UserInDB
from ..schemas.users import UserInResponse, UserInCreate

from ..models.recipes import RecipeInDB, RecipeCategory
from ..schemas.recipes import RecipeInResponse, RecipeInCreate


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserInResponse).filter(UserInResponse.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserInResponse).filter(UserInResponse.email == email).first()


# WIP hash password
def create_user(db: Session, user: UserInCreate):
    hashed_password = user.password
    db_user = UserInDB(
        username=user.username,
        nickname=user.nickname,
        email=user.email,
        hashed_password=hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(RecipeInResponse).filter(RecipeInResponse.id == recipe_id).first()


def create_recipe(db: Session, recipe: RecipeInCreate):
    db_recipe = RecipeInDB()
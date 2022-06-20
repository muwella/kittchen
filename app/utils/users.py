# SQLAlchemy
from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
# fastapi
from fastapi import Depends
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate, UserInUpdate
# db
from ..utils.dependencies import get_db


# WIP raise exceptions
    # user doesn't exist
    # email is already in use
    # incorrect email or password


def create_user(user: UserInCreate, db: Session):
    hashed_password = 'hashed_' + user.password

    user_in_db = UserInDB(
        **user.dict(exclude={'password'}),
        hashed_password=hashed_password
        )

    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)

    # it should not return UserInDB, but i'm testing
    return {}


def get_user_by_id(user_id: int, db: Session) -> UserInDB:
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(email: str, db: Session) -> UserInDB:
    return db.query(UserInDB).filter(UserInDB.email == email).first()


def update_user(user: UserInUpdate, db: Session):
    return {}


def verify_email_exists(email: str, db: Session):
    return db.query(UserInDB.query.filter(UserInDB.email == email).exists()).scalar()


def verify_login_match(email: str, password: str, db: Session):
    user = get_user_by_email(email, db)
    
    # WIP encripted password
    db_password = user.hashed_password

    return password == db_password
    

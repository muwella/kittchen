# SQLAlchemy
from sqlalchemy.orm import Session
# fastapi
from fastapi import Depends
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate
# db
from ..utils.dependencies import get_db

# NOTE i can just write 'db = Depends(get_db)'
    # instead of 'db: Session = Depends(get_db)'


def verify_email_exists():
    pass


def verify_email_password_match():
    pass


def get_user_by_id(
    db: Session,
    user_id: int
    ):
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(
    db: Session,
    email: str
    ):
    return db.query(UserInDB).filter(UserInDB.email == email).first()


def save_user(user: UserInCreate, db = Depends(get_db())):
    hashed_password = 'hashed_' + user.password

    # DOUBT .dict excludes password by itself?
        # because there's no password field on UserInDB
    user_in_db = UserInDB(
        **user.dict(),
        hashed_password=hashed_password
        )

    # user_in_db = UserInDB(
    #     email = user.email,
    #     nickname = user.nickname,
    #     hashed_password = hashed_password
    # )

    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)

    # WIP it should not return UserInDB, but i'm testing
    return user_in_db

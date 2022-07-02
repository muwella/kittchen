# python
from typing import Union
# SQLAlchemy
from sqlalchemy.orm import Session
# fastapi
from fastapi import Depends
from fastapi import HTTPException
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate, UserInUpdate, UserInLogin
# password encryption
from passlib.hash import bcrypt


# WIP raise exceptions
    # user doesn't exist
    # email is already in use


# create

def create_user(user: UserInCreate, db: Session):
    user_in_db = UserInDB(
        **user.dict(exclude={'password'}),
        hashed_password=bcrypt.hash(user.password)
    )

    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)

    return {'user in db': user_in_db}


# read

def get_user_by_id(user_id: int, db: Session) -> UserInDB:
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(email: str, db: Session) -> (Union[UserInDB, None]):
    return db.query(UserInDB).filter(UserInDB.email == email).first()


def get_users_by_id(users_id: list[int], db: Session):
    return db.query(UserInDB).filter(UserInDB.id in users_id).all()


# update

def update_user(user: UserInUpdate, user_id: int, db: Session):
    return {}


# delete

def delete_user(user_id: int, db: Session):
    db.delete()
    pass


# verifications

def verify_email_exists(email: str, db: Session):
    return db.query(UserInDB.query.filter(UserInDB.email == email).exists()).scalar()


def verify_login_match(user: UserInLogin, db: Session):
    if verify_email_exists(user.email, db) is None:
        raise HTTPException(status_code=404, detail='Email not found')
    else:
        user_in_db = get_user_by_email(user.email, db)

        return bcrypt.verify(user.password, user_in_db.hashed_password)
    

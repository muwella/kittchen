# python
from typing import Union
# SQLAlchemy
from sqlalchemy.orm import Session
# models (DB) & schemas
from ..models.users import UserInDB
from ..schemas.users import UserInCreate, UserInUpdate
# password encryption
from passlib.hash import bcrypt


# create

def create_user(
    user: UserInCreate,
    db: Session
):
    # create user instance
    user_in_db = UserInDB(
        **user.dict(exclude={'password'}),
        hashed_password=bcrypt.hash(user.password)
    )

    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)

    return {'user': user_in_db}


# read

def get_user_by_id(user_id: int, db: Session) -> UserInDB:
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_username(username: str, db: Session) -> Union[UserInDB, None]:
    return db.query(UserInDB).filter(UserInDB.username == username).first()


def get_user_by_email(email: str, db: Session) -> Union[UserInDB, None]:
    return db.query(UserInDB).filter(UserInDB.email == email).first()


def get_users_by_id(users_id: list[int], db: Session):
    return db.query(UserInDB).filter(UserInDB.id in users_id).all()


# update

def update_user(user_update: UserInUpdate, user_in_db: UserInDB, db: Session):
    if user_update.nickname:
        user_in_db.nickname = user_update.nickname
    
    if user_update.password:
        user_in_db.hashed_password = bcrypt.hash(user_update.password)

    db.commit()
 
    return get_user_by_id(user_in_db.id, db)


# delete

def delete_user(user: UserInDB, db: Session):
    db.delete(user)
    db.commit()


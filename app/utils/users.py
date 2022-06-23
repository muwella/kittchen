# SQLAlchemy
from sqlalchemy.orm import Session
# fastapi
from fastapi import Depends
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate, UserInUpdate, UserInLogin


# WIP raise exceptions
    # user doesn't exist
    # email is already in use
    # incorrect email or password


# create

# WIP encripted password
def create_user(user: UserInCreate, db: Session):
    hashed_password = 'hashed_' + user.password

    user_in_db = UserInDB(
        **user.dict(exclude={'password'}),
        hashed_password=hashed_password
    )

    db.add(user_in_db)
    db.commit()
    db.refresh(user_in_db)

    return {'user in db': user_in_db}


# read

def get_user_by_id(user_id: int, db: Session) -> UserInDB:
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(email: str, db: Session) -> UserInDB:
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


# WIP encripted password
def verify_login_match(user: UserInLogin, db: Session):
    user = get_user_by_email(user.email, db)
    
    db_password = user.hashed_password

    return user.password == db_password
    

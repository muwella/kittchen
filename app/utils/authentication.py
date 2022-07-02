# SQLAlchemy
from sqlalchemy.orm import Session
# fastapi
from fastapi import HTTPException
# models
from ..models.users import UserInDB
from ..schemas.users import UserInLogin, UserInResponse
# utils
from .users import get_user_by_email
# password encryption
from passlib.hash import bcrypt


# verifications

def email_exists(email: str, db: Session):
    return get_user_by_email(email, db).exists().scalar()


def passwords_match(password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)


# WIP user has to have an username
def verify_login(user: UserInLogin, db: Session):

    if not email_exists(user.email, db):
        raise HTTPException(status_code=404, detail='Email not found')
    else:
        user_in_db = get_user_by_email(user.email, db)
        if not passwords_match(user.password, user_in_db.hashed_password):
            raise HTTPException(status_code=401, detail='Invalid password')

    # WIP for testing
    return user_in_db
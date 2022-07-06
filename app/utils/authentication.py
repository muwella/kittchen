# SQLAlchemy
from sqlalchemy.orm import Session
# fastapi
from fastapi import HTTPException
# models
from ..schemas.users import UserInResponse
# utils
from .dependencies import get_db
from .users import get_user_by_username
# password encryption
from passlib.hash import bcrypt


def passwords_match(password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)


def authenticate_user(username: str, password: str, db: Session):
    '''Verifies username and password and logs in an user.'''

    user_db = get_user_by_username(username, db)
    if user_db is None:
        raise HTTPException(status_code=404, detail='Invalid username')
    else:
        if not passwords_match(password, user_db.hashed_password):
            raise HTTPException(status_code=401, detail='Invalid password')
        else:
            user_response = UserInResponse.from_orm(user_db)

            return user_response

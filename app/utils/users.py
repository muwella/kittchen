# SQLAlchemy
from sqlalchemy.orm import Session
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate


def verify_email_exists():
    pass


def verify_email_password_match():
    pass


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserInDB).filter(UserInDB.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserInDB).filter(UserInDB.email == email).first()


# WIP hash password
def create_user(db: Session, user: UserInCreate):
    hashed_password = user.password
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
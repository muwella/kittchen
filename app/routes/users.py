# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path
from fastapi import status, HTTPException

from app.models.users import UserInDB
# models
from ..schemas.users import UserInCreate, UserInResponse, UserInUpdate
# SQLAlchemy
from sqlalchemy.orm import Session
from ..config.database import conn
# utils & dependencies
from ..utils import users
from ..utils.dependencies import get_db, verify_token
from ..config.security import oauth2_scheme


# router

router = APIRouter(
    prefix = '/users',
    tags=['users']
)


# endpoints

@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserInCreate = Body(),
    db: Session = Depends(get_db)
):
    user_in_db = users.get_user_by_email(user_in.email, db)

    if user_in_db is not None:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    return users.create_user(user_in, db)


@router.get(
    '/{user_id}', 
    # response_model=UserInResponse,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def get_user(
    user_id: int = Path(gt=0),
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2_scheme)
):
    user_in_db = users.get_user_by_id(user_id, db)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail='User not found')

    return conn.execute((UserInDB.__table__).select()).fetchall()


@router.put(
    '/{user_id}/update', 
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def update_user(
    user_id: int = Path(gt=0),
    user: UserInUpdate = Body(),
    db: Session = Depends(get_db)
    # token: str = Depends(oauth2_scheme)
):
    users.update_user(user, user_id, db)
    return get_user(user_id, db)


@router.delete(
    '/{user_id}/delete',
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def delete_user(
    user_id: int = Path(gt=0),
    # token: str = Depends(oauth2_scheme)
):
    return {}
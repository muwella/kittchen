# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path
from fastapi import status, HTTPException
# SQLAlchemy
from sqlalchemy.orm import Session
# utils & dependencies
from ..utils import users
from ..utils.dependencies import get_db, verify_token
from ..config.security import oauth2_scheme
# models (DB) & schemas
from ..schemas.users import UserInCreate, UserInResponse, UserInUpdate


# router

router = APIRouter(
    prefix='/users',
    tags=['users']
)


# DB attributes that get excluded in UserInResponse
db_excluded_attributes = {
    'hashed_password',
    'token'
}


# endpoints

@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserInCreate = Body(),
    db: Session = Depends(get_db)
):
    user_in_db = users.get_user_by_username(user_in.username, db)
    if user_in_db:
        raise HTTPException(status_code=400, detail='Username is already in use')

    user_in_db = users.get_user_by_email(user_in.email, db)
    if user_in_db:
        raise HTTPException(status_code=400, detail='Email is already in use')
    
    users.create_user(user_in, db)

    return {'HTTP status': status.HTTP_201_CREATED}


@router.get(
    '/{user_id}', 
    response_model=UserInResponse,
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

    return UserInResponse.from_orm(user_in_db)


@router.put(
    '/{user_id}/update',
    # response_model=UserInResponse,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def update_user(
    user_id: int = Path(gt=0),
    user: UserInUpdate = Body(),
    db: Session = Depends(get_db)
    # token: str = Depends(oauth2_scheme)
):
    user_in_db = users.get_user_by_id(user_id, db)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    user_in_db = users.update_user(user, user_in_db, db)

    return user_in_db
    return UserInResponse.from_orm(user_in_db)


@router.delete(
    '/{user_id}/delete',
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def delete_user(
    user_id: int = Path(gt=0),
    db: Session = Depends(get_db)
    # token: str = Depends(oauth2_scheme)
):
    user_in_db = users.get_user_by_id(user_id, db)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    users.delete_user(user_in_db, db)

    return {'HTTP status': status.HTTP_200_OK}
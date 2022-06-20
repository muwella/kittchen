# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path
from fastapi import status, HTTPException
import fastapi
# models
from ..schemas.users import UserInCreate, UserInResponse, UserInUpdate
# SQLAlchemy
from sqlalchemy.orm import Session
# utils & dependencies
from ..utils import users
from ..utils.dependencies import get_db, verify_token
from ..utils.security import oauth2_scheme


# router

# LOOKUP tags, dependencies, responses
router = APIRouter(
    prefix = '/user',
    tags=['users']
)


# endpoints

# LOOKUP status_code responses
@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserInCreate = Body(),
    db: Session = Depends(get_db)
):
    user_in_db = users.get_user_by_email(user_in.email, db)

    if user_in_db:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    return users.create_user(user_in, db)


# FIXME issue with sending user_id as an int
    # without {user_id} and a Path() field
    # also cannot send it as Body() bc of GET
# @router.get(
#     '/me', 
#     response_model=UserInResponse,
#     status_code=status.HTTP_200_OK,
#     # dependencies=[Depends(verify_token)]
# )
# def get_user_me(
#     user_id: int,
#     db: Session = Depends(get_db),
#     # token: str = Depends(oauth2_scheme)
# ):
#     user_in_db = users.get_user_by_id(user_id, db)
#     if user_in_db is None:
#         raise HTTPException(status_code=404, detail='User not found')

#     return user_in_db


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

    return user_in_db


# WIP how to update an existing user
@router.put(
    'me/update', 
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def update_user(
    user: UserInUpdate = Body(),
    # token: str = Depends(oauth2_scheme)
):
    return {}


@router.delete(
    'me/delete',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(verify_token)]
)
def delete_user(
    user_id: int
):
    return {}
# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path
from fastapi import status, HTTPException
# models
from ..models.users import UserInDB
from ..schemas.users import UserInCreate, UserInResponse
# SQLAlchemy
# from sqlalchemy.orm import Session
# utils & dependencies
from ..utils.users import *
from ..utils.dependencies import verify_token
from ..utils.security import oauth2_scheme


# router

router = APIRouter(
    prefix = '/user',
    # dependencies=[Depends(verify_token)],
    # tags=['users']
    # responses={404: {"description": "Not found"}}
)


# endpoints

@router.post(
    '/new',
    # response_model = UserInResponse,
    # status_code = status.HTTP_201_CREATED
    )
def create_user(
    user_in: UserInCreate,
    dependencies=[Depends(save_user)]
    ):
    user_in_db = save_user(user_in)

    return {'UserIn': user_in, 'UserInDB': user_in_db}


# DOUBT do i get ID as a simple int? Or as smth else
# @router.get(
#     '/profile/me',
#     response_model = UserInResponse,
#     status_code = status.HTTP_200_OK,
#     dependencies = [Depends(verify_token)]
#     )
# def get_user_me(token: str = Depends(oauth2_scheme)):
#     return {'testing': 'oauth2'}


# @router.get('/profile/{user_id}')
# def get_user(user_id: int = Path(gt=0)):
#     if user_id not in ['foo', 'bar']:
#         raise HTTPException(status_code=404, detail='User not found')
#     return get_user(user_id)


# WIP check for unique username in DB
    # also password & confirmation (new) email to change email
# @router.put('/profile/me/edit')
# def update_user(user_update: UserInCreate = Body()):
#     return {}
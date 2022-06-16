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

placeholder_list = ['foo', 'bar']

# WIP divide dependencies by users, ingredients, recipes, etc.

# NOTE i can import dependencies that
    # are gonna be used by every endpoint
router = APIRouter(
    prefix = '/user',
    dependencies=[Depends(verify_token)],
    # tags=['users']
    # responses={404: {"description": "Not found"}}
)


# NOTE i can just write 'db = Depends(get_db)'
    # instead of 'db: Session = Depends(get_db)'
# NOTE using 'dependencies = [Depends(...),...]'
    # it doesn't return anything (as in db)
@router.post(
    '/new',
    response_model = UserInResponse,
    status_code = status.HTTP_201_CREATED
    )
def create_user(
    user_in: UserInCreate,
    ):
    # hash password
    hashed_password = 'hashed' + user_in.password
    # save user in DB
        # .dict() unwraps the pydantic model UserIn and
        # allows us to fill another model with the data
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)

    return {'user in DB': user_in_db}


# DOUBT do i get ID as a simple int? Or as smth else
@router.get(
    '/profile/me',
    response_model = UserInResponse,
    status_code = status.HTTP_200_OK,
    dependencies = [Depends(verify_token)]
    )
def get_user_me(token: str = Depends(oauth2_scheme)):
    return {'testing': 'oauth2'}


# @router.get('/profile/{user_id}')
# def get_user(user_id: int = Path(gt=0)):
#     if user_id not in placeholder_list:
#         raise HTTPException(status_code=404, detail='User not found')
#     return get_user(user_id)


# WIP check for unique username in DB
    # also password & confirmation (new) email to change email
# @router.put('/profile/me/edit')
# def update_user(user_update: UserInCreate = Body()):
#     return {}
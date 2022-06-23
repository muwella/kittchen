# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Form
# models
# dependencies
# from ..utils.dependencies import oauth2_scheme

router = APIRouter(
    prefix='/login',
    tags=['login']
)

### LOGIN


# @router.post('/')
# def login(
#     token: str = Depends(oauth2_scheme)
#     # username: str = Form(),
#     # password: str = Form()
# ):
#     # check for username in DB
#     # verify username and password match
#     return {'ok': 'ok'}

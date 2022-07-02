# FastAPI
from http.client import HTTPException
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# SQLAlchemy
from sqlalchemy.orm import Session
# models
from app.models.users import UserInDB
# utils
from ..utils.authentication import verify_login

# WIP generate token with JSON Web Tokens

router = APIRouter(tags=['token'])

# tokenURL: the endpoint that creates the token
# oauth2_scheme looks for the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_login(form_data.username, form_data.password)

    

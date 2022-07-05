# FastAPI
from http.client import HTTPException
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# SQLAlchemy
from sqlalchemy.orm import Session
# utils
from ..utils.dependencies import get_db
from ..utils.authentication import authenticate_user
# JSON Web Token
import jwt

JWT_SECRET = 'myjwtsecret'

router = APIRouter(tags=['token'])

# tokenURL: the endpoint that creates the token
# oauth2_scheme looks for the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@router.post('/token')
def generate_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    user_response = authenticate_user(form_data.username, form_data.password, db)
    
    # FIXME can't use dict on SQLAlchemy model (UserInDB), how to extract info?
    token = jwt.encode(user_response.dict(), JWT_SECRET)

    return {'access_token': token, 'token_type': 'bearer'}

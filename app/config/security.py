from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# WIP generate token with JSON Web Tokens

router = APIRouter(tags=['token'])

# tokenURL: the endpoint that creates the token
# oauth2_scheme looks for the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@router.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


# example
@router.get('/')
def index(token: str = Depends(oauth2_scheme)):
    return {'the token': token}

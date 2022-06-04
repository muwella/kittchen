# FastAPI
from fastapi import APIRouter
from fastapi import Form
# models
# dependencies

router = APIRouter(
    prefix='/login',
    tags=['login']
)

### LOGIN


@router.post('/')
def login(
    username: str = Form(),
    password: str = Form()
):
    # check for username in DB
    # verify username and password match
    return {'nickname': username}

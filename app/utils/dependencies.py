# database
from ..database.database import SessionLocal
from fastapi import Header, HTTPException
# from fastapi.security import OAuth2PasswordBearer

# dependencies are functions that give certain endpoints
    # certain things that they need
    # without repeating code a hundred times

# WIP Bigger Applications - Multiple files: dependencies

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# WIP fake token
def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
# database
from ..database.database import SessionLocal
from fastapi import Header, HTTPException

# dependencies are functions that give to certain endpoints
    # certain things that they need without repeating code

# WIP Bigger Applications - Multiple files: dependencies

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# WIP fake token
def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")




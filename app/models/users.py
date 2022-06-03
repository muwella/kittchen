# SQLite
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from ..database import Base

# WIP i have to rethink the DB relations

# DOUBT should i have a mix of BaseModel classes
    # for requests and Base classes for DB?
# ANSWER SQLAlchemy models are gonna be models, and
    # Pydantic models are gonna be schemas


# SQLAlchemy models

# WIP hashed password
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    nickname: Column(String)
    email: Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    hashed_password: Column(String)

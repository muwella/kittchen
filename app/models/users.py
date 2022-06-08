# SQLite
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# TBD if an user deactivates their account
    # and wants it back, how should i proceed?

# SQLAlchemy models

# WIP hashed password
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email: Column(String, unique=True, index=True)
    nickname: Column(String)
    hashed_password: Column('password', String)
    is_active = Column(Boolean, default=True)
    
    # token: str
    
    recipes = relationship('RecipeInDB', back_populates='creator')

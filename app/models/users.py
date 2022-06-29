# SQLAlchemy
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    nickname = Column(String(255))
    hashed_password = Column('password', String(255))
    is_active = Column(Boolean, default=True)
    token = Column(String(255))
    
    recipes = relationship('RecipeInDB', back_populates='creator')


# WIP hashed password, token
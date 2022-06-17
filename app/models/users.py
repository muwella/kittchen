# SQLite
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# SQLAlchemy models

# WIP hashed password
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True, index=True)
    nickname = Column(String(64))
    hashed_password = Column('password', String(64))
    is_active = Column(Boolean, default=True)
    
    # token= str
    
    recipes = relationship('RecipeInDB', back_populates='creator')

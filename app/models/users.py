# SQLite
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# if an user deactivates their account and wants it back,
# when they enter their login credentials they'll see
# a notice asking them to confirm if they want to
# reactivate their account.

# when an account is deactivated, all of their recipes
# get hidden, and their friends will not be able to
# see them anymore

# if the account gets reactivated, everything goes
# back to normal


# SQLAlchemy models

# WIP hashed password
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email: Column(String, unique=True, index=True)
    nickname: Column(String)
    hashed_password: Column('password', String)
    is_active = Column(Boolean, default=True)
    
    # token: str
    
    recipes = relationship('RecipeInDB', back_populates='creator')

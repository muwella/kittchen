from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# DOUBT do i need to access UserInDB in Recipe?
from .users import UserInDB


# TBD should make:
# - a Recipe model
# - a RecipeCategory model
# - and a RecipeCustomCategory model?

# and if i do, should i have RecipeCategory as an Enum
    # and RecipeCustomCategory as another table for users?


class RecipeCategory(Base):
    id = Column(Integer, primary_key=True, index=True)
    __tablename__ = 'recipe categories'


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    steps = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship('UserInDB', back_populates='recipes')
    # category = relationship()

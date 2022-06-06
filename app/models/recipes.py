from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column
from sqlalchemy.orm import relationship # LOOKUP relationship

from ..database.database import Base

from .ingredients import Ingredient

# SQLAlchemy models

# WIP create my own categories that i'll
    # share with every user
# created by me and by users
class RecipeCategory(Base):
    __tablename__ = 'recipe_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    creator_id = Column('creator', Integer, ForeignKey('users.id'))


# DOUBT is it list(Ingredient) legal? should be
# ANSWER no haha
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ingredients = Column(list(Ingredient))
    steps = Column(String)

    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')
    # category = relationship('RecipeCategory', back_populates='category')

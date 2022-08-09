# SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
# from .recipe_ingredients import RecipeIngredient
# database
from ..config.database import Base

# SQLAlchemy models


### DEPRECATED ###
# class RecipeIngredient(Base):
#     __tablename__ = 'recipe_ingredient'

#     recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
#     ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)


# Many-To-Many recipe/ingredient relationship
RecipeIngredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)


# DOUBT why did I put ingredientInDB in here
class IngredientInDB(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_default = Column(Boolean, default=True)
    creator_id = Column('creator', Integer, ForeignKey('users.id'), default=1)
    category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))


class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    steps = Column(String, default='')
    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')
    category = relationship('RecipeCategoryInDB', back_populates='recipes')
    ingredients = relationship('IngredientInDB', secondary=RecipeIngredient)


# One-To-Many relationship:
    # Parent class has: children = relationship('Child', back_populates='parent')
    # Child class has:
       # ForeignKey to Parent.id
       # parent = relationship('Parent', back_populates='children')

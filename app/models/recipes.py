# SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

'''
    One-To-Many relationship
    
    Parent class has: children = relationship('Child', back_populates='parent')
    Child class has:
        ForeignKey to Parent.id
        parent = relationship('Parent', back_populates='children')
'''

'''
    Many-To-Many relationship
    
    I create an association table between RecipeInDB and IngredientInDB: RecipeIngredient
    (later it'll have restrictions concerning creators' IDs when it's not a default ingredient)

    There are two ways of doing a Table like this in SQLAlchemy
    and to make a Many-To-Many rship I needed to use this one
'''

RecipeIngredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)


# DOUBT do i need to have IngredientInDB in here in order to
    # make the compound table work?
class IngredientInDB(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    creator_id = Column('creator', Integer, ForeignKey('users.id'), default=1)
    is_default = Column(Boolean, default=True)
    # category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))

    creator = relationship('UserInDB', back_populates='ingredients')
    # category = relationship('IngredientCategoryInDB', back_populates='ingredients')


class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    steps = Column(String(255), default='')
    creator_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    # category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')
    ingredients = relationship('IngredientInDB', secondary=RecipeIngredient)
    # category = relationship('RecipeCategoryInDB', back_populates='recipes')


### DEPRECATED ### recipe_ingredient table that didn't work
# class RecipeIngredient(Base):
#     __tablename__ = 'recipe_ingredient'
#
#     recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
#     ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)


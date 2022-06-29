# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .recipe_ingredients import RecipeIngredient
# database
from ..config.database import Base

# SQLAlchemy models

class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    steps = Column(String, default='')
    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')
    category = relationship('RecipeCategoryInDB', back_populates='recipes')
    ingredients = relationship('IngredientsInDB', secondary=RecipeIngredient, backref='recipes')


# One-To-Many relationship:
    # Parent class has: children = relationship('Child', back_populates='parent')
    # Child class has:
       # ForeignKey to Parent.id
       # parent = relationship('Parent', back_populates='children')

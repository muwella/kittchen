# SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

RecipeIngredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)


# DOUBT IngredientInDB in here so the compound table works?
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


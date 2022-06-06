from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column
from sqlalchemy.orm import relationship

from ..database.database import Base

# SQLAlchemy models

# created only by me
class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))
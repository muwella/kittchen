from pydantic import validator
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column
from sqlalchemy.orm import relationship

from ..config.database import Base

# SQLAlchemy models

# created only by me
class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'
    
    id = Column(Integer, primary_key=True, index=True)
    # name = Column(String)

    # @validator('id')
    # def positive_id(cls, v):
    #     if v < 0:
    #         raise ValueError('id must be positive')
    #     return v.title()



class IngredientInDB(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    # name = Column(String)

    # category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))
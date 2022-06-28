from sqlalchemy import Column, ForeignKey, Integer, String
from ..config.database import Base
from sqlalchemy.orm import relationship

# SQLAlchemy models

# default categories by kittchen; users do not create their own
class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

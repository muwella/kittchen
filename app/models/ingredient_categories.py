# SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

# default categories by kittchen; users do not create their own
class IngredientCategoryInDB(Base):
    __tablename__ = 'ingredient_categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


# WIP default categories:
#   - fruits & vegetables
#   - cereal & legumes
#   - meat & dairy
#   - fish & eggs?
#   - sweets & fats
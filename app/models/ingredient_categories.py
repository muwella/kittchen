# SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

# NOTE default categories by kittchen; users do not create their own

#### LATER ####

# class IngredientCategoryInDB(Base):
#     __tablename__ = 'ingredient_categories'
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)



# TBD which food categories?

# WIP default categories:
#   - cereal & legumes
#   - fruits & vegetables
#   - meat & dairy
#   - fish & eggs?
#   - sweets & fats
#   - other

# WIP to put on DB:
# Cereals = 0
# Fruits = 1
# Vegetables = 2
# Dairy = 3
# Meat = 4
# Fats = 5
# Other = 6

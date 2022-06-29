# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
# database
from ..config.database import Base

# SQLAlchemy models

class RecipeCategoryInDB(Base):
    __tablename__ = 'recipe_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_default = Column(Boolean, default=True)
    creator_id = Column('creator', Integer, ForeignKey('users.id'))

    recipes = relationship('RecipeInDB', back_populates='category')


# WIP default recipe categories:
#   - meal
#   - dessert
#   - no category
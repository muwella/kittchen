from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# SQLAlchemy models

class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    steps = Column(String, default='')
    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')

    
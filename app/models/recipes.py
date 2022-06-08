from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from ..database.database import Base

# SQLAlchemy models

# WIP create default categories
class RecipeCategory(Base):
    __tablename__ = 'recipe_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_default = Column(Boolean, default=False)

    # creator_id = Column('creator', Integer, ForeignKey('users.id'))


class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    steps = Column(String, default='')
    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    # category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')
    # category = relationship('RecipeCategory', back_populates='category')

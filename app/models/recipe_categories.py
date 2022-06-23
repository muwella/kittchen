from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

from ..config.database import Base

# SQLAlchemy models

# WIP add default 'meal' and 'dessert' categories

class RecipeCategoryInDB(Base):
    __tablename__ = 'recipe_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_default = Column(Boolean, default=False)

    creator_id = Column('creator', Integer, ForeignKey('users.id'))

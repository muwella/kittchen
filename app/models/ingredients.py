from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column
from ..config.database import Base
from sqlalchemy.orm import relationship

# SQLAlchemy models

class IngredientInDB(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    creator_id = Column('creator', Integer, ForeignKey('users.id'), default=1)
    category_id = Column('category', Integer, ForeignKey('ingredient_categories.id'))
    is_default = Column(Boolean, default=True)

    # category = 


# default recipe categories:
#   - meal
#   - dessert
#   - no category
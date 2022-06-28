from sqlalchemy import Column, ForeignKey, Integer, String
from ..config.database import Base
from sqlalchemy.orm import relationship

# SQLAlchemy models

class RecipeInDB(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    steps = Column(String, default='')
    creator_id = Column('creator', Integer, ForeignKey('users.id'))
    category_id = Column('category', Integer, ForeignKey('recipe_categories.id'))

    creator = relationship('UserInDB', back_populates='recipes')

    # def __repr__(self) -> str:
    #     return f"Recipe(id={self.id!r},name={self.name!r})"
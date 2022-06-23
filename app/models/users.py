# SQLite
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship

from ..config.database import Base

# SQLAlchemy models

# WIP hashed password
# WIP token
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    nickname = Column(String(255))
    hashed_password = Column('password', String(64))
    is_active = Column(Boolean, default=True)
    
    # token = str
    
    recipes = relationship('RecipeInDB', back_populates='creator')

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r},email={self.email!r}, nickname={self.nickname!r})"
# SQLite
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

# TBD if an user deactivates their account
    # and wants it back, how should i proceed?

# SQLAlchemy models

# WIP hashed password
# WIP relationships
class UserInDB(Base):
    __tablename__ = 'users'
    
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String(128), unique=True)
    nickname: Column('nickname', String(128))
    email: Column('email', String(512), unique=True, index=True)
    is_active = Column('is active', Boolean, default=True)
    hashed_password: Column('password', String)

    # recipes = relationship('Recipe', back_populates='creator')

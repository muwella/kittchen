from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./kittchen.db"

# if I were to use PostgreSQL, I'd have to uncomment the line:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# and adapt it to my DB and credentials

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# the argument 'connect_args={"check_same_thread": False}'
    # is needed only for SQLite, not other DBs

# sessionmaker creates a database session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# later we'll inherit from this class to create each
    # of the DB models
Base = declarative_base()

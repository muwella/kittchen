from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlite database:
SQLALCHEMY_DATABASE_URL = "sqlite:///./kittchen.db"

# postgreSQL database:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# MySQL database:
# SQLALCHEMY_DATABASE_URL = "mysql+pymsql://root:password@localhost:3306/db"
    # on terminal: pip install pymsql
    # if MySQL is installed on docker, the connection is different

# the argument 'connect_args' is needed only for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# to interact with db
conn = engine.connect()

# sessionmaker creates a database session instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# NOTE FatSecret Platform API -> will most probably use it
# LOOKUP user-agent, HTTP proxy, middleware
# FIXME use Schemas in routes instead of DB Models
# NOTE find a better way to import Base

from fastapi import FastAPI
from .routes import users, recipes, login, ingredients
from .config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(recipes.router)
# app.include_router(login.router)
# app.include_router(ingredients.router)

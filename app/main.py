# LOOKUP user-agent, HTTP proxy, middleware

from fastapi import FastAPI
from .config import security
from .routes import users, recipes, ingredients, recipe_categories, main
from .config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(main.router)
app.include_router(security.router)
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(ingredients.router)
app.include_router(recipe_categories.router)

# run local server: uvicorn app.main:app --reload
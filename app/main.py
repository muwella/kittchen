from fastapi import FastAPI
from .routers import login, users, recipes, ingredients

# LATER FatSecret Platform API -> will most probably use it

# LOOKUP
# user-agent, HTTP proxy, middleware

# FIXME use Schemas in routes instead of DB Models

# WIP relationships

app = FastAPI()

# app.include_router(login.router)
app.include_router(users.router)
app.include_router(recipes.router)
# app.include_router(ingredients.router)
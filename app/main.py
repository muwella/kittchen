from fastapi import FastAPI
from .routers import login, users#, recipes, ingredients

# LOOKUP
# FatSecret Platform API -> will most probably use it
# frozenset
# user-agent, HTTP proxies

# FIXME some issue with models and schemas in recipes

app = FastAPI()

app.include_router(login.router)
app.include_router(users.router)
# app.include_router(recipes.router)
# app.include_router(ingredients.router)
#Python
from lib2to3.pytree import Base
from typing import Optional
#Pydantic
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI, Body

app = FastAPI() # app is an instance of FastAPI


# MODELS
# unique? foreign key? passwords?
# class User(BaseModel):
#     name: str
#     username: str
#     password: str


# class IngredientCategory(BaseModel):
#     name: str


# class Ingredient(BaseModel):
#     name: str
#     category: IngredientCategory


class RecipeCategory(BaseModel):
    name: str


class Recipe(BaseModel):
    title: str
    # ingredients: list[Ingredient]
    steps: Optional[str] = None
    category: RecipeCategory


# PATH OPERATION
@app.get("/") # path operation decorator
def home(): # path operation function
    return {"Hello": "World"}

# una API transmite info por JSON
# path/route/endpoint: lo que se agrega a la url del dominio

# HTTP:
    # header
    # body
    # operations

    # operations principales:
        # GET
        # POST
        # PUT
        # DELETE

    # operations más complejas
        # OPTIONS
        # HEAD
        # PATCH
        # TRACE


# PATH PARAMETERS -> obligatory
# "path/something/{recipe_id}"


# QUERY PARAMETERS -> optional
# "path/users/{user_id}/details?age=21&height=159"


# REQUEST & RESPONSE BODY
@app.post("/recipe/new")
def create_recipe(recipe: Recipe = Body(...)):
    return recipe
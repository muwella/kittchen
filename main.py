#Python
import json
from typing import Optional, Union, List
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field, EnumError, EmailStr
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Cookie, status

# LOOKUP fastapi routerAPI
# LOOKUP FatSecret Platform API -> will most probably use it
# WIP integrate SQL DB

app = FastAPI()

# models

# WIP email field
# WIP hash password (security)
class UserBase(BaseModel):
    nickname: str = Field(
        min_length=1,
        max_length=50,
        example='Maru'
    )
    username: str = Field(
        min_length=1,
        max_length=50,
        example='muwella'
    )
    # email: EmailStr = Field(
    #    regex="^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
    #    )


class User(UserBase):
    password: str


class UserOut(UserBase):
    pass


class IngredientCategory(Enum):
    cereals = 'cereals'
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'
    meat = 'meat'
    fats = 'fats'


class Ingredient(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example='banana'
    )
    category: IngredientCategory = Field(
        default=None,
        example='fruit'
    )


class RecipeCategory(Enum):
    meal = 'meal'
    dessert = 'dessert'


# TBD tags, likes, comments
# TBD modify recipes of others?
class Recipe(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example="Noodles"
    )
    ingredients: List[Ingredient] = Field(
        default=[],
        example=[1,2,3]
    )
    steps: Union[str, None] = Field(
        default=None,
        example="Boil, eat, repeat"
    )
    category: Union[RecipeCategory, None] = Field(
        default=None,
        example="meal"
    )


# HTTP methods

@app.get('/')
def root():
    return {"message": "hello world"}


# TBD should i receive user_id to look for their recipes
    # or use a token? (is there a token in the GET header?)
@app.get('/recipes')
def show_recipes(
    name: Union[str, None] = Query(default=None),
    ingredients: Union[List[int], None] = Query(default=None),
    category: Union[RecipeCategory, None] = Query(default=None)
    ):

    # look for recipes with query filters
    return {'all': 'recipes'}


@app.post('/recipes/new')
def create_recipe(recipe: Recipe = Body()):
    return {'New recipe': recipe}


@app.get('/recipes/{recipe_id}')
def show_recipe(recipe_id: int = Path(
        gt=0,
        title='Recipe',
        description='Shows a recipe'
        )
    ):
    return {"recipe_id": recipe_id}


@app.put('/recipes/{recipe_id}/edit')
def update_recipe(
    recipe_id: int = Path(
        title='Recipe',
        description='Updates a recipe',
        gt=0
        ),
    recipe: Recipe = Body(),
    ):
    # edit recipe
    return {recipe_id: recipe}


# show all ingredients
@app.get('/ingredients')
def show_ingredients(
    name: Union[str, None] = Query(default=None),
    category: Union[IngredientCategory, None] = Query(default=None)
    ):

    # look for ingredients with query filters
    return {name: category}


@app.post('/ingredients/new')
def create_ingredient(ingredient: Ingredient = Body()):
    return {'new': 'ingredient'}


@app.get('/ingredients/{ingredient_id}')
def show_ingredient(
    ingredient_id: int = Path(
        gt=0,
        title='Ingredient',
        description='Shows an ingredient'
        )
    ):
    return {"ingredient_id": ingredient_id}


# TBD only if it's a custom ingredient?
# NOTE if we use FatSecret API maybe we won't need to customize ingredients
@app.put('/ingredients/{ingredient_id}/edit')
def update_ingredient(
    ingredient_id: int = Path(
        title='Ingredient',
        description='Updates an ingredient',
        gt=0
        ),
    ingredient: Ingredient = Body(),
    ):
    # edit ingredient
    return {ingredient_id: Ingredient}



# db
def db_ingredientes():
    ing = [
        Ingredient('Banana', IngredientCategory.fruit),
        Ingredient('Peach', IngredientCategory.fruit),
        Ingredient('Pear', IngredientCategory.fruit),
        Ingredient('Apple', IngredientCategory.fruit),
    ]



## apuntes ##

# DUDAS
# unique? foreign key? passwords?
# integrate to DB? how to CRUD DB?
# deploy on heroku

# HTTP:
    # header
    # body
    # methods / "operations"
        # POST - create
        # GET - read
        # PUT- update
        # DELETE - delete

        # OPTIONS
        # HEAD
        # PATCH
        # TRACE

# path/route/endpoint: lo que se agrega a la url del dominio

# PATH PARAMETERS -> mandatory
    # "path/something/{recipe_id}"
# QUERY PARAMETERS -> optional
    # "path/users/{user_id}/details?age=21&height=159"

# REQUEST & RESPONSE BODY
    # @app.post("/recipe/new")
    # def create_recipe(recipe: Recipe = Body()):
    #     return recipe

# Si necesito algo obligatorio es PATH PARAMETER
# No QUERY PARAMETER
# Puede pasar que lo necesite en algun caso
    # (un QUERY PARAMETER obligatorio)
    # Pero es raro, aunque se puede

# VALIDATIONS - Parámetros
    # min_length
    # max_length
    # regex

    # ge (greater or equal than) >=
    # le (less or equal than) <=
    # gt (greater than) >
    # lt (less than) <

    # SWAGGER
        # title
        # description

# get.put: # el cliente tiene que enviar un REQUEST BODY a la API

# config class is for API testing
# class Config:
#     schema_extra = {
#         "example": {
#             "name": "Noodles",
#             "steps": "Boil and eat",
#             "category": 'meal'
#         }
#     }

# example parameter is also for API testing

# return 2 dicts on 1 JSON (recipe_id & recipe)
    # results = recipe_id.dict()
    # results.update(recipe.dict())
    # return results

# HTTP Status code
    # 100 Information
    # 200 OK
        # 201 Created
        # 204 No content
    # 300 Redirect
    # 400 Client error
        # 404 No exists
        # 422 Validation error
    # 500 Internal Server Error
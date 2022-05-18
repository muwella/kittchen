#Python
from typing import Optional, Union, List
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field, EmailStr
#FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()


# models

# unique? foreign key? passwords?
class User(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example='Maru'
    )
    username: str = Field(
        min_length=1,
        max_length=50,
        example='muwella'
    )
    password: str


class IngredientCategory(Enum):
    cereals = 'cereals'
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'
    meat = 'meat'
    fats = 'fats'
    other = 'other'


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


# example parameter is for API testing 
class Recipe(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
        example="Noodles"
        )
    ingredients: List[Ingredient] = []
    # ingredients: list[Ingredient]
    steps: Optional[str] = Field(
        default=None,
        example="Boil and eat"
        )
    category: Optional[RecipeCategory] = Field(
        default=None,
        example="meal"
        )

    # config class is for API testing
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Noodles",
    #             "steps": "Boil and eat",
    #             "category": 'meal'
    #         }
    #     }

class Location(BaseModel):
    city: str
    state: str
    country: str


## apuntes ##

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

# path/route/endpoint: lo que se agrega a la url del dominio

# PATH PARAMETERS -> mandatory
    # "path/something/{recipe_id}"
# QUERY PARAMETERS -> optional
    # "path/users/{user_id}/details?age=21&height=159"

# REQUEST & RESPONSE BODY
    # @app.post("/recipe/new")
    # def create_recipe(recipe: Recipe = Body()):
    #     return recipe


# HTTP operations

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recipes")
def show_recipes(q: Union[str, None] = None):
    return {"q": q}


@app.get("/recipes/{recipe_id}")
def show_recipe(recipe_id: int, q: Union[str, None] = None):
    return {"recipe_id": recipe_id, "q": q}


@app.post("/recipe/new")
def create_recipe(recipe: Recipe = Body()):
    return recipe


# VALIDATIONS - QUERY PARAMETERS
@app.get("/recipe/detail")
def show_recipe(
    title: str = Query(
        min_length=1,
        max_length=50,
        title='Recipe title',
        description='A recipe with steps'
        ),
    steps: Optional[str] = Query(
        None,
        title='Recipe steps',
        description="It explains how to do the recipe"
        )
    ):
    return {title: steps}


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


# VALIDATIONS - PATH PARAMETERS
@app.get("/recipe/detail/{recipe_id}")
def show_recipe(
    recipe_id: int = Path(
        gt=0,
        title='Recipe',
        description='Shows a recipe'
        )
    ):
    return {recipe_id: 'ok'}


# VALIDATIONS - REQUEST BODY
@app.put("/recipe/{recipe_id}")
# el cliente tiene que enviar un REQUEST BODY a la API
def update_recipe(
    recipe_id: int = Path(
        title='Recipe',
        description='Updates a recipe',
        gt=0
        ),
    recipe: Recipe = Body(),
    ):
    # return 2 dicts on 1 JSON
    # results = recipe_id.dict()
    # results.update(recipe.dict())
    return recipe

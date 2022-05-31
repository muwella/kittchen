#app
from .models.users import UserIn, UserInDB, UserOut
from .models.ingredients import IngredientCategory, Ingredient
from .models.recipes import RecipeCategory, Recipe
#Python
from uuid import UUID
# from datetime import datetime, time, timedelta
from typing import Union
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Header, Cookie
from fastapi import status

# LOOKUP fastapi routerAPI (use @router instead of @app)
# LOOKUP FatSecret Platform API -> will most probably use it
# LOOKUP: Path, Query, Header, Cookie, Body, Form, File, Field
# WIP integrate SQL DB

# NOTE with attribute example I can add an invalid
    # example that I know will fail, to test? i guess
    # Would be better actually testing tho
    # BUT! it's good for documentation

# LOOKUP frozenset
# LOOKUP user-agent, HTTP proxies

# NOTE I can declare with which model I'm responding
    # with @app.smth('', response_model=MyModel)
    # probably CREATE and POST
    # could also be =list, or anything
    # it gets documented

app = FastAPI()


# HTTP methods

### ROOT

@app.get('/')
def root():
    return {"message": "hello world"}



### USER

@app.post('/users/new')
def create_user(user_in: UserIn):
    # hash password
    hashed_password = 'hashed' + user_in.password
    # save user in DB
        # .dict() unwraps the pydantic model UserIn and
        # allows us to fill another model with the data
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)

    return {'user in DB': user_in_db}



### LOGIN

@app.post('/login')
def login(
    username: str = Form(),
    password: str = Form()
):
    # check for username in DB
    # verify username and password match
    return {'nickname': username}


### RECIPES

# TBD should i receive user_id to look for their recipes
    # or use a token? (is there a token in the GET header?)
@app.get('/recipes')
def show_recipes(
    name: Union[str, None] = Query(
        default=None,
        min_length=1,
        max_length=50
        ),
    ingredient: Union[list[int], None] = Query(
        default=None,
        alias='ing'
        ),
    category: Union[RecipeCategory, None] = None
    ):

    # look for recipes with query filters
    response = {
        'status': status.HTTP_200_OK,
        'name': name,
        'ingredients': ingredient,
        'category': category
    }

    return response


# DOUBT que pasa si no recibo algo que entre dentro del modelo Recipe?
# WIP advanced user guide: return status code
    # other from the default
@app.post('/recipes/new', status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: Recipe):
    return {'all': 'received'}


@app.get('/recipes/{recipe_id}')
def show_recipe(recipe_id: int = Path(
        gt=0,
        title='Recipe',
        description='Shows a recipe'
        )
    ):
    return {"recipe_id": recipe_id}


# LOOKUP the user may click Update when in reality didn't
    # change anything, so should I make Recipe optional?
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



### INGREDIENTS

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



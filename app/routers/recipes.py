# Python
from typing import Union
# FastAPI
from fastapi import APIRouter
from fastapi import Query, Path, Body
from fastapi import status
# models
from ..models.recipes import RecipeInDB, RecipeCategory
# dependencies


router = APIRouter(
    prefix='/recipes'
)


### RECIPES

# TBD should i receive user_id to look for their recipes
    # or use a token? (is there a token in the GET header?)

# FIXME commented because of DB
# @router.get('/')
# def show_recipes(
#     name: Union[str, None] = Query(
#         default=None,
#         min_length=1,
#         max_length=50
#         ),
#     ingredient: Union[list[int], None] = Query(
#         default=None,
#         alias='ing'
#         ),
#     category: Union[RecipeCategory, None] = None
#     ):

#     # look for recipes with query filters
#     response = {
#         'status': status.HTTP_200_OK,
#         'name': name,
#         'ingredients': ingredient,
#         'category': category
#     }

#     return response


# DOUBT que pasa si no recibo algo que entre dentro del modelo Recipe?
# WIP advanced user guide: return status code
    # other from the default
# WIP should be able to add an image to a recipe

# FIXME commented because of DB
# @router.post('/recipes/new', status_code=status.HTTP_201_CREATED)
# def create_recipe(recipe: Recipe):
#     return {'all': 'received'}


# FIXME commented because of DB
# @router.get('/recipes/{recipe_id}')
# def show_recipe(recipe_id: int = Path(
#         gt=0,
#         title='Recipe',
#         description='Shows a recipe'
#         )
#     ):
#     return {"recipe_id": recipe_id}


# LOOKUP the user may click Update when in reality didn't
    # change anything, so should I make Recipe optional?

# FIXME commented because of DB
# @router.put('/recipes/{recipe_id}/edit')
# def update_recipe(
#     recipe_id: int = Path(
#         title='Recipe',
#         description='Updates a recipe',
#         gt=0
#         ),
#     recipe: Recipe = Body(),
#     ):
#     # edit recipe
#     return {recipe_id: recipe}

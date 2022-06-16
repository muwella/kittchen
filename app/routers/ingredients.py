# Python
from typing import Union
# FastAPI
from fastapi import APIRouter
from fastapi import Query, Body, Path
# models
from ..schemas.ingredients import Ingredient, IngredientCategory


router = APIRouter(
    prefix='/ingredients'
)

### INGREDIENTS

# # show all ingredients
# @router.get('/ingredients')
# def show_ingredients(
#     name: Union[str, None] = Query(default=None),
#     category: Union[IngredientCategory, None] = Query(default=None)
#     ):

#     # look for ingredients with query filters
#     return {name: category}


# @router.post('/ingredients/new')
# def create_ingredient(ingredient: Ingredient = Body()):
#     return {'new': 'ingredient'}


# @router.get('/ingredients/{ingredient_id}')
# def show_ingredient(
#     ingredient_id: int = Path(
#         gt=0,
#         title='Ingredient',
#         description='Shows an ingredient'
#         )
#     ):
#     return {"ingredient_id": ingredient_id}


# TBD only if it's a custom ingredient?
# NOTE if we use FatSecret API maybe we won't need to customize ingredients
# @router.put('/ingredients/{ingredient_id}/edit')
# def update_ingredient(
#     ingredient_id: int = Path(
#         title='Ingredient',
#         description='Updates an ingredient',
#         gt=0
#         ),
#     ingredient: Ingredient = Body(),
#     ):
#     # edit ingredient
#     return {ingredient_id: Ingredient}

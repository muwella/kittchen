# FastAPI
from fastapi import APIRouter
from fastapi import Query, Path, Body
from fastapi import status
# models
from ..models.recipes import RecipeInDB
# from ..models.recipe_categories import RecipeCategoryInDB
from ..schemas.recipes import RecipeInCreate
from ..schemas.recipe_categories import RecipeCategoryInCreate
# dependencies


router = APIRouter(
    prefix='/recipe_categories',
    tags=['recipe_categories']
)


### RECIPE CATEGORIES


@router.get('/')
def show_recipe_category():
    return {}

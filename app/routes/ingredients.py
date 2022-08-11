# Python
from typing import Union
# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path, Query
from fastapi import status, HTTPException
# SQLAlchemy
from sqlalchemy.orm import Session
# utils & dependencies
from ..utils import ingredients
from ..utils.dependencies import get_db, verify_token
from ..config.security import oauth2_scheme
# models (DB) & schemas
from ..schemas.ingredients import IngredientInCreate, IngredientInResponse, IngredientInUpdate


# router

router = APIRouter(
    prefix='/ingredients'
)


# endpoints

@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
    # dependencies=[Depends(verify_token)]
)
def create_ingredient(
    ingredient_in: IngredientInCreate = Body(),
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2_scheme)
):

    return {'HTTP status': status.HTTP_201_CREATED}



@router.get('/ingredients')
def get_ingredients(
    name: Union[str, None] = Query(default=None),
    ):

    return {}


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

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
    prefix='/ingredients',
    tags=['ingredients']
)


# endpoints

@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
    # dependencies=[Depends(verify_token)]
)
def create_ingredient(
    user_id: int,
    ingredient_in: IngredientInCreate = Body(),
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2_scheme)
):
    ingredient_in_db = ingredients.get_ingredient_by_name(ingredient_in.name, user_id, db)
    if ingredient_in_db:
        raise HTTPException(status_code=400, detail='Ingredient already exists')
    
    ingredients.create_ingredient(ingredient_in, user_id, db)
    
    return {'HTTP status': status.HTTP_201_CREATED}


# WIP QUERY
@router.get(
    '/{ingredient_id}', 
    response_model=IngredientInResponse,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def get_ingredient(
    ingredient_id: int = Path(gt=0),
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2_scheme)
):
    ingredient_in_db = ingredients.get_ingredient_by_id(ingredient_id, db)
    if ingredient_in_db is None:
        raise HTTPException(status_code=404, detail='Ingredient not found')

    return IngredientInResponse.from_orm(ingredient_in_db)


# WIP QUERY - get ingredients plural? ingredients/filter?
@router.get('/ingredients')
def get_ingredients(
    name: Union[str, None] = Query(default=None),
    ):

    return {}


@router.put(
    '/{ingredient_id}/update',
    response_model=IngredientInResponse,
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def update_ingredient(
    ingredient_id: int = Path(gt=0),
    ingredient_update: IngredientInUpdate = Body(),
    db: Session = Depends(get_db)
    # token: str = Depends(oauth2_scheme)
):
    ingredient_in_db = ingredients.get_ingredient_by_id(ingredient_id, db)
    if ingredient_in_db is None:
        raise HTTPException(status_code=404, detail='Ingredient not found')
    
    ingredient_in_db = ingredients.update_ingredient(ingredient_update, ingredient_in_db, db)

    return IngredientInResponse.from_orm(ingredient_in_db)


@router.delete(
    '/{ingredient_id}/delete',
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(verify_token)]
)
def delete_ingredient(
    ingredient_id: int = Path(gt=0),
    db: Session = Depends(get_db)
    # token: str = Depends(oauth2_scheme)
):
    ingredient_in_db = ingredients.get_ingredient_by_id(ingredient_id, db)
    if ingredient_in_db is None:
        raise HTTPException(status_code=404, detail='Ingredient not found')
    
    ingredients.delete_ingredient(ingredient_in_db, db)

    return {'HTTP status': status.HTTP_200_OK}

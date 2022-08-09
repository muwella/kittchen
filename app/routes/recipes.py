# FastAPI
from fastapi import APIRouter, Depends
from fastapi import Body, Path, Query
from fastapi import status, HTTPException
# SQLAlchemy
from sqlalchemy.orm import Session
# utils & dependencies
from ..utils import recipes
from ..utils.dependencies import get_db, verify_token
# models (DB) & schemas
from ..models.recipes import RecipeInDB
from ..schemas.recipes import RecipeInCreate, RecipeInResponse, RecipeInUpdate


# router

router = APIRouter(
    prefix='/recipes',
    tags=['recipes']
)


# endpoints

@router.post(
    '/new',
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(
    recipe_in: RecipeInCreate = Body(),
    db: Session = Depends(get_db)
):
    # DOUBT would they be any problem creating a new recipe?
        # it doesn't have any UNIQUE constraint

    recipes.create_recipe(recipe_in, db)

    return {'HTTP status': status.HTTP_201_CREATED}



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

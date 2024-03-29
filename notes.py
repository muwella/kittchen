# User Guide
    # 26 entries
    # para el 12 de junio: 13 días
    # 2 entradas mínimo por día
# Advanced User Guide
    # 37 entries
    # para el 28 de junio: 16 días
    # 2 a 3 entradas mínimo por día

# PROXIMO: request files

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


# You can declare multiple Form parameters in a
# path operation, but you can't also declare Body fields
# that you expect to receive as JSON, as the request
# will have the body encoded using
    # application/x-www-form-urlencoded
# instead of
    # application/json.
# This is part of the HTTP protocol.


# NOTE with attribute example I can add an invalid
    # example that I know will fail, to test? i guess
    # Would be better actually testing tho
    # BUT! it's good for documentation


# NOTE I can declare with which model I'm responding
    # with @app.smth('', response_model=MyModel)
    # probably CREATE and POST
    # could also be =list, or anything
    # it gets documented


# HANDLING ERRORS
# possible errors:
# - the client doesn't have enough privileges for that operation
# - the client doesn't have access to that resource
# - the item the client was trying to access doesn't exist

# normaly, you responde with 400s HTTP status code (400 to 499)


# NOTE using 'dependencies = [Depends(...),...]'
    # it doesn't return anything (as in db)
    # (on path operation functions)

# NOTE to save an user in DB
    # .dict() unwraps the pydantic model UserInCreate and
    # allows us to fill another model with the data
    # in this case, it fills up UserInDB

# -----

# LATER: deactivate and reactivate accounts
# if an user deactivates their account and wants it back,
# when they enter their login credentials they'll see
# a notice asking them to confirm if they want to
# reactivate their account.

# when an account is deactivated, all of their recipes
# get hidden, and their friends will not be able to
# see them anymore

# if the account gets reactivated, everything goes
# back to normal

# -----

# NOTE i can just write 'db = Depends(get_db)'
    # instead of 'db: Session = Depends(get_db)'

# -----

# En los esquemas de Pydantic de respuesta (orm_mode = True)
# Las instancias de objeto de esas clases tienen que crearse con "from_orm"
# obj = PydanticModel.from_orm(ModelInDB)

# -----

# Old Procfile heroku deploy:
    # web: uvicorn main:app --host 0.0.0.0 --port $PORT
# New Procfile heroku deploy:
    # web: uvicorn main:app --host 0.0.0.0 --port=${PORT:-5000}

# -----
    
'''
    One-To-Many relationship
    
    Parent class has: children = relationship('Child', back_populates='parent')
    Child class has:
        ForeignKey to Parent.id
        parent = relationship('Parent', back_populates='children')
'''

'''
    Many-To-Many relationship
    
    I create an association table between RecipeInDB and IngredientInDB: RecipeIngredient
    (later it'll have restrictions concerning creators' IDs when it's not a default ingredient)

    There are two ways of doing a Table like this in SQLAlchemy
    and to make a Many-To-Many rship I needed to use this one:

    TableName = Table(
        'table_name',
        Base.metadata,
        Column('column_name', DataType, ForeignKey('table.id'), primary_key=True),
        Column('column_name', DataType, ForeignKey('table.id'), primary_key=True)
    )

'''

# -----

### DEPRECATED ### recipe_ingredient table that didn't work
# class RecipeIngredient(Base):
#     __tablename__ = 'recipe_ingredient'
#
#     recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
#     ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)

# -----

# WIP to create recipes, ingredients and their relationships!!

 # Rows in RecipeInDB and IngredientInDB get created as normal
        # recipe = RecipeInDB(...)
        # ingredient1 = IngredientInDB(...)
        # db.session.add_all([recipe, ingredient1])
        # db.session.commit()
    
    # Then
        # recipe.ingredients.append(ingredient1)
        # db.session.commit()

    # to remove item:
        # recipe.ingredients.remove(ingredient1)
        # db.session.commit()

# -----
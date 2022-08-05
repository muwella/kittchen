# Kittchen

### what it is
(WIP)
REST API Python FastAPI project

### what it does
(WIP)

## Quickstart
(WIP)
requires venv
on kittchen directory, activate venv
  pip install -r requirements.txt

## Run it
(WIP)
This project uses uvicorn as ASGI server
Run the server with:
  $ uvicorn main:app --reload

You can see the automatic interactive API documentation

## Project structure
  app
  ├── config            
  │   ├── database.py
  │   └── security.py 
  ├── models
  │   ├── images.py ?
  │   ├── ingredient_categories.py
  │   ├── ingredients.py
  │   ├── recipe_categories.py
  │   ├── recipe_ingredients.py
  │   ├── recipes.py
  │   └── users.py
  ├── routes
  │   ├── ingredients.py
  │   ├── main.py ?
  │   ├── recipe_categories.py
  │   ├── recipes.py
  │   └── users.py
  ├── schemas
  │   ├── ingredients.py
  │   ├── recipe_categories.py
  │   ├── recipes.py
  │   └── users.py
  ├── utils
  │   ├── authentication.py
  │   ├── dependencies.py
  │   ├── errors.py
  │   ├── recipes_categories.py
  │   ├── recipes_ingredients.py
  │   ├── recipes.py
  │   └── users.py
  ├── main.py          - FastAPI application creation and configuration.
 

## Thanks

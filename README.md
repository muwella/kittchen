# Kittchen

### What it is
Kittchen is a REST API Python app with it's recently developed FastAPI framework.

### What it does
Kittchen is a personal project intended for solving issues with time management, balancing productivity and wellbeing with an organised diet and a thought out nutrition.

It allows the user to keep track of their favorite recipes, their shopping needs, and to plan meals faster and easier.

It's ultimate goal it's to remove time loss and meal-prepping-centred worried thoughts!

## Quickstart
On Windows:

* On C:/your/path/to/kittchen directory, create a virtual environment:

```
python -m venv venv
```

* Activate it on C:/your/path/to/kittchen directory:

```
venv\Scripts\activate
```

* Once is activated, install project requirements:

```
pip install -r requirements.txt
```

## Run it
This project uses uvicorn as ASGI server. Run the server with:

```
$ uvicorn main:app --reload
```

You can see the automatic interactive API documentation on your localhost: http://127.0.0.1:8000/docs

## Project structure
(WIP)

    app
    ├── config
    │   ├── database.py
    │   └── security.py 
    ├── models                          - ORM models (SQLAlchemy) 
    │   ├── ingredient_categories.py
    │   ├── ingredients.py
    │   ├── recipe_categories.py
    │   ├── recipe_ingredients.py
    │   ├── recipes.py
    │   └── users.py
    ├── routes                          - API routing
    │   ├── ingredients.py
    │   ├── main.py ?
    │   ├── recipe_categories.py
    │   ├── recipes.py
    │   └── users.py
    ├── schemas                         - Pydantic models
    │   ├── ingredients.py
    │   ├── recipe_categories.py
    │   ├── recipes.py
    │   └── users.py
    ├── utils                           - CRUD and other essencials
    │   ├── authentication.py
    │   ├── dependencies.py
    │   ├── errors.py
    │   ├── recipes_categories.py
    │   ├── recipes_ingredients.py
    │   ├── recipes.py
    │   └── users.py
    └── main.py                         - FastAPI application creation and configuration.


## Thanks

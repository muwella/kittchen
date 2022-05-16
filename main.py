from fastapi import FastAPI #FastAPI is a class

app = FastAPI() # app is an instance of FastAPI


# PATH OPERATION
@app.get("/") # path operation decorator
def home(): # path operation function
    return {"Hello": "World"}

# una API transmite info por JSON
# path/route/endpoint: lo que se agrega a la url del dominio

# HTTP:
    # header
    # body
    # operations

    # operations principales:
        # GET
        # POST
        # PUT
        # DELETE

    # operations más complejas
        # OPTIONS
        # HEAD
        # PATCH
        # TRACE


# PATH PARAMETERS -> obligatory
# "path/something/{recipe_id}"


# QUERY PARAMETERS -> optional
# "path/users/{user_id}/details?age=21&height=159"


# REQUEST & RESPONSE BODY
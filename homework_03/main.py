import json
from fastapi import FastAPI

app = FastAPI()

@app.get('/ping/')
def view():
    return {"message": "pong"}


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

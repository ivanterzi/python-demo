import json
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/ping/')
def view():
    return {"message": "pong"}


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

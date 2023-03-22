import tensorflow as tf
from nsk.models import get_model, get_result
from fastapi import FastAPI, Request, Body
# from fastapi.staticfiles import StaticFiles

MODEL = get_model()
app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def get_index(request: Request):
    info = {
        "name":"NSK API",
        "model":"nsk_model_v1",
        "description": "Nuoseklių sakinių klasifikavimas",
        "endpoint": "/api/predict",
        "content-type": "application/json",
        "body": "{'abstract':'abstarct sentences without new lines'}",
    }
    
    return info


@app.post("/api/predict")
async def get_predictions(request: Request, body=Body(...)):
    abstract = body['abstract']
    outputs = get_result(abstract, MODEL)

    return outputs
import tensorflow as tf
from nsk.models import get_model
from nsk.data import format_input_data, format_output_data
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
    inputs = format_input_data(abstract)
    pred_probs = MODEL.predict(x=inputs)
    outputs = format_output_data(abstract, pred_probs)

    return outputs
import tensorflow as tf
from nsk.models import get_model, get_result
from fastapi import FastAPI, Request, Body, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

MODEL = get_model()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    context = {
        "request": request,
        "abstract": "",
        "results": "",
    }
    
    return templates.TemplateResponse("index.html", context)


@app.post("/", response_class=HTMLResponse)
async def get_html_predictions(request: Request, abstract: str=Form()):
    results = get_result(abstract, MODEL, group=True)
    
    context = {
       "request": request,
       "abstract": abstract,
       "results": results,
    }
    
    return templates.TemplateResponse("index.html", context) 
    
@app.post("/api/predict")
async def get_predictions(request: Request, body=Body(...)):
    abstract = body['abstract']
    outputs = get_result(abstract, MODEL)

    return outputs
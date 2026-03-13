from fastapi import FastAPI
from basics_pydantic import Patient
from fastapi.responses import JSONResponse
import json

def save_data(data):
    with open("medical.json",'a') as f:
        json.dump(data,f)

app=FastAPI()

@app.post("/create")
def create(patient:Patient):
    data=patient.model_dump()
    data=data[0]
    save_data(data)
    return JSONResponse(status_code=201,content={'message':"Data is stored succesfully"})


from fastapi import FastAPI,Path,HTTPException
import json

app=FastAPI()

def load_data():
    with open('medical.json','r') as f:
        data=json.load(f)

    return data    

@app.get('/')
def hello():
    return {"message":"hello to all the medical patient"}

@app.get('/about')
def about():
    return {"message":"This is the medical website"}

@app.get('/fetch')
def fetch():
    data=load_data()
    return data

@app.get('/patient/{patient_name}')
def fetch_patient(patient_name: str=Path(...,title="the",description="Give the name in lower or uppercase")):
    data = load_data()

    for patient in data:
        if patient["name"].lower() == patient_name.lower():
            return patient

    raise HTTPException(404,"Data not found")
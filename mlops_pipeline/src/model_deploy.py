# model_deploy.py
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

# Load model and preprocessing
MODEL_PATH = "/app/mlops_pipeline/models/best_model.pkl"
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Telco Churn Model API")

# Define input schema
class InputRecord(BaseModel):
    data: dict

class BatchInput(BaseModel):
    data: List[dict]

@app.get("/")
def root():
    return {"message": "API operativa. Usa /predict"}

@app.post("/predict")
def predict(input_data: BatchInput):
    df = pd.DataFrame(input_data.data)

    # Predicción
    preds = model.predict(df)

    return {
        "input_rows": len(df),
        "predictions": preds.tolist()
    }

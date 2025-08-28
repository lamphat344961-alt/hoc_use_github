from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("loan_model.pkl", "rb") as f:
    model = pickle.load(f)

# Định nghĩa schema input
class LoanData(BaseModel):
    age: int
    income: float
    loan_amount: float

@app.get("/")
def home():
    return {"message": "Loan Risk API is running 🚀"}

@app.post("/predict")
def predict(data: LoanData):
    X = np.array([[data.age, data.income, data.loan_amount]])
    pred = model.predict(X)[0]
    return {
        "input": data.dict(),
        "prediction": "approve ✅" if pred == 1 else "deny ❌"
    }

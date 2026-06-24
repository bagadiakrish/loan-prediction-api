from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("loan_model.pkl")
class LoanData(BaseModel):
    Dependents: int
    ApplicantIncome:float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Gender_Male: int
    Married_Yes: int
    Education_Not_Graduate: int
    Self_Employed_Yes: int
    Property_Area_Semiurban: int
    Property_Area_Urban: int

@app.get("/")
def home():
    return {"message": "Loan Prediction API Running"}


@app.post("/predict")
def predict(data: LoanData):

    input_data = [[
        data.Dependents,
        data.ApplicantIncome,
        data.CoapplicantIncome,
        data.LoanAmount,
        data.Loan_Amount_Term,
        data.Credit_History,
        data.Gender_Male,
        data.Married_Yes,
        data.Education_Not_Graduate,
        data.Self_Employed_Yes,
        data.Property_Area_Semiurban,
        data.Property_Area_Urban
    ]]

    prediction = model.predict(input_data)
    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"
    return {
        "prediction": result
    }
@app.get("/health")
def health():
    return {"Status": "Healthy"}

@app.get("/model-info")
def model_info():
    return {
        "model":"Loan Prediction",
        "algorithm":"Logistic Regression"
    }
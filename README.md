# Loan Prediction API

Machine Learning project built using Python, Scikit-Learn and FastAPI.

## Features

- Predicts loan approval status
- Logistic Regression Model
- FastAPI Backend
- Interactive Swagger UI

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- FastAPI
- Uvicorn

## Run Project

```bash
uvicorn app:app --reload
```

Open:

http://127.0.0.1:8000/docs

## API Endpoint

POST /predict

Returns:

```json
{
  "prediction":"Loan Approved"
}
```
## Live Demo

https://loan-prediction-api.onrender.com

## API Documentation

https://loan-prediction-api.onrender.com/docs
## Author

Krish Bagadia

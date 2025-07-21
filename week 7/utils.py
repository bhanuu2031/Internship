import pickle
import pandas as pd

def load_model(path="model/trained_model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def make_prediction(model, input_data: pd.DataFrame):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)
    return prediction, proba

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap

from utils import load_model, make_prediction

st.set_page_config(page_title="Flower Predictor", layout="centered")
st.title("🌼 Iris Flower Predictor")

# Load model
model = load_model()

# User inputs
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Create input DataFrame
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                          columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])

# Prediction
if st.button("Predict"):
    prediction, proba = make_prediction(model, input_data)
    
    st.subheader("Prediction")
    st.write(f"🌟 Predicted Species: **{prediction[0]}**")
    
    st.write("🔍 Class Probabilities:")
    st.bar_chart(pd.DataFrame(proba, columns=model.classes_).T)


import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Car_Model.pkl")

st.title("Car Price Category Prediction")

car_age = st.number_input(
    "Enter the Car Age",
    min_value=0.0,
    value=5.0,
    step=1.0
)

kilometers_driven = st.number_input(
    "Enter the Kilometers Driven",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Car_Age": [car_age],
        "Kilometers_Driven": [kilometers_driven]
    })

    prediction = model.predict(input_data)

    pred = prediction[0]

    st.success(f"Predicted Price Category: {pred}")

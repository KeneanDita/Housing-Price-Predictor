import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load("regressor_1.pkl")

st.title("🏠 California House Price Predictor")

st.write("Enter the property details below to estimate the house price.")

longitude = st.number_input("Longitude", value=-122.23, step=0.01)
latitude = st.number_input("Latitude", value=37.88, step=0.01)
housing_median_age = st.number_input("Housing Median Age", value=20.0)
total_rooms = st.number_input("Total Rooms", value=2000.0)
total_bedrooms = st.number_input("Total Bedrooms", value=400.0)
population = st.number_input("Population", value=1000.0)
households = st.number_input("Households", value=400.0)
median_income = st.number_input("Median Income (10k USD)", value=3.0, step=0.1)



if st.button("Predict Price"):
    input_data = np.array([[longitude, latitude, housing_median_age,
                            total_rooms, total_bedrooms, population,
                            households, median_income]])
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Value: **${prediction:,.2f}**")

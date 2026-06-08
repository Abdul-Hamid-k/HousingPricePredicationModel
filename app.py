from HousingPricePredicationModel import USA_HousingPricePredicationModel
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('USA_Housing.csv')

st.header("Housing Price Estimater (USA)")
st.write("##### You can get an estimation of housing price in USA based on the below paramertes.")
st.write("We are assuring you of `90+ %` accuracy.")

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem; /* Adjust value as needed */
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.write("All this below question are regarding the society that you want housing around.")

avgAreaIncome  = st.number_input('Average Area Income', step=1)
avgHouseAge = st.number_input('Average House Age', min_value=2, max_value=10, step=1)
avgNumRooms = st.number_input('Average Number of Rooms', min_value=3, max_value=11, step=1)
areaPopulation = st.number_input('Area Population', min_value=25000, step=100)

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem; /* Adjust value as needed */
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Estimate Price"):
    if avgAreaIncome and avgHouseAge and avgNumRooms and areaPopulation:
        res = USA_HousingPricePredicationModel(avgAreaIncome, avgHouseAge, avgNumRooms, areaPopulation)
        if res <= 0:
            st.error("Failed to estimate price")
        else:
            st.success(f"Estimated Housing price: $ {res} (USD)")




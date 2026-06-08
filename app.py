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

avgAreaIncome  = st.number_input('Average Area Income')
avgHouseAge = st.number_input('Average House Age', min=2, max=10)
avgNumRooms = st.number_input('Average Number of Rooms', min=3, max=11)
areaPopulation = st.number_input('Area Population')

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem; /* Adjust value as needed */
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

if avgAreaIncome and avgHouseAge and avgNumRooms and areaPopulation:
    res = USA_HousingPricePredicationModel(avgAreaIncome, avgHouseAge, avgNumRooms, areaPopulation)
    if res <= 0:
        st.error("Failed to estimate price")
    else:
        st.sucess(f"Estimated Housing price: {res)} $ (USD)")




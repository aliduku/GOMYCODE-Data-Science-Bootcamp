import streamlit as st

weight = st.number_input("Please enter your weight in kilograms:")
height = st.number_input("Please enter your height in meters:")

if st.button("Calculate"):
    BMI = weight / (height**2)
    st.text(f"According to your weight of {weight}kg and height of {height}m.\nYour BMI is {BMI:.2f}.")
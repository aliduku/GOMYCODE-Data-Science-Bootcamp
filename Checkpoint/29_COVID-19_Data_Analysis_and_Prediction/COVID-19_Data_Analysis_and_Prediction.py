import streamlit as st
import pandas as pd
import joblib
import os

# Load the best model
best_model = joblib.load('GBR_model.pkl')

# Create a Streamlit app
st.title("COVID-19 Case Prediction App")
st.sidebar.header("Input Features")

# Add input features to the sidebar
hospitalized_currently = st.sidebar.slider("Currently Hospitalized", min_value=0, max_value=200000, value=10000)
icu_currently = st.sidebar.slider("Currently in ICU", min_value=0, max_value=40000, value=5000)
ventilator_currently = st.sidebar.slider("Currently on Ventilator", min_value=0, max_value=15000, value=3000)
death_increase = st.sidebar.slider("Daily Death Increase", min_value=0, max_value=7000, value=1000)
hospitalized_increase = st.sidebar.slider("Daily Hospitalization Increase", min_value=0, max_value=20000, value=2000)
negative_increase = st.sidebar.slider("Daily Negative Test Increase", min_value=0, max_value=1000000, value=50000)
total_test_results_increase = st.sidebar.slider("Daily Total Test Results Increase", min_value=0, max_value=3000000, value=100000)

# Add a button to start prediction
if st.sidebar.button("Predict"):
    # Apply the same preprocessing pipeline to user input
    pipeline = joblib.load('preprocessing_pipeline.pkl')
    user_input_features = [[
        hospitalized_currently, icu_currently, ventilator_currently,
        death_increase, hospitalized_increase, negative_increase,
        total_test_results_increase
    ]]
    user_input_features = pipeline.transform(user_input_features)

    # Make predictions and display results
    prediction = best_model.predict(user_input_features)
    st.sidebar.markdown(f"<p style='font-size: 24px;'>Predicted Number Positive of Cases: {int(prediction[0])}</p>", unsafe_allow_html=True)

# Read all images from the "visualizations" folder
visualization_folder = "visualizations"
visualization_images = [f for f in os.listdir(visualization_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
visualization_images.sort()

# Display visualizations
st.header("COVID-19 Data Visualizations")

for image_filename in visualization_images:
    image_path = os.path.join(visualization_folder, image_filename)
    st.image(image_path, use_column_width=True)
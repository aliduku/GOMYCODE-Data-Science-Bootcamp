import pickle
import streamlit as st

# Load the saved model
with open('iris_rf_model.pkl', 'rb') as file:
    saved_model = pickle.load(file)

# Create a dictionary to map class numbers to flower names
class_to_flower = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# Create a Streamlit app
st.title("Iris Flower Type Prediction")
st.header("Enter the measurements of the iris flower:")

# Input fields for sepal length, sepal width, petal length, and petal width
sepal_length = st.slider("Sepal Length", 3.0, 10.0)
sepal_width = st.slider("Sepal Width", 2.0, 6.0)
petal_length = st.slider("Petal Length", 1.0, 8.0)
petal_width = st.slider("Petal Width", 0.0, 3.0)

# Prediction button
if st.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = saved_model.predict(input_data)
    flower_type = class_to_flower[prediction[0]]
    st.write(f"The predicted type of iris flower is: {flower_type}")
import streamlit as st
from PIL import Image

st.title("Hello Gomycode")
st.header("Headers")
st.subheader("Subheaders")
st.text("Text")
st.markdown("# Text")
st.success("Well done!")
st.info("Info")
st.error("Error")
st.warning("warning")
st.exception("exception")

image = Image.open("img.png")
st.image(image, width = 800)

if st.checkbox("Turn On/Off"):
    st.text("Turned on.")
else:
    st.text("Turned off.")

status = st.radio("Please choose your gender:", ("Male", "Female"))

if status == "Male":
    st.text("Male selected.")
else:
    st.text("Female selected.")

Hobbies = st.selectbox("Hobbies", ["Volley", "Football", "Basketball", "Swimming"])
st.text(f"Hobby selected is {Hobbies}")

Hobbies = st.multiselect("Hobbies", ["Volley", "Football", "Basketball", "Swimming"])
st.text(f"Hobbies selected are {len(Hobbies)}")

if st.button("Button"):
    st.text("Button pressed.")
    
age = st.text_input("Please enter your age:", placeholder = "Age")

if st.button("Submit"):
    st.text("Submitted.")
    result = age.title()
    st.text(f"Age is {result}")

level = st.slider("Select:", 1, 5)

st.text(f"Level is {level}")
import streamlit as st
from datetime import date

st.title("Widgets Playground")
st.write("Explore different Streamlit widgets.")

name=st.text_input("Enter your name")
age=st.number_input("Enter your age",1,100,20)
marks=st.slider("Select your marks",0,100,75)

city=st.selectbox(
    "Choose your city",
    ["Chennai","Mumbai","Delhi"]
)

skills=st.multiselect(
    "Select your skills",
    ["Python","Machine Learning","SQL","Streamlit"]
)

gender=st.radio(
    "Select your gender",
    ["Male","Female","Other"]
)

agree=st.checkbox("I agree to the terms")
dob=st.date_input(
    "Select your date of birth",
    date(2000,1,1)
)

uploaded_file=st.file_uploader("Upload a file")

if st.button("Submit"):
    st.subheader("Your Details")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Marks:",marks)
    st.write("City:",city)
    st.write("Skills:",skills)
    st.write("Gender:",gender)
    st.write("Agreed to terms:",agree)
    st.write("Date of birth:",dob)

    if uploaded_file is not None:
        st.write("Uploaded file:",uploaded_file.name)
    else:
        st.info("No file uploaded.")
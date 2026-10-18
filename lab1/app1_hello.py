import streamlit as st

st.set_page_config(
    page_title="Hello App",
    page_icon="👋",
    layout="centered"
)

st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")

st.write("Streamlit converts Python scripts into web apps.")
st.markdown("**Bold text**,*Italic text*, and `code` work here.")

st.success("App loaded successfully!")
st.info("This is an information message.")
st.warning("This is a warning message.")
st.error("This is an error message.")

name=st.text_input("Enter your name")
age=st.number_input("Enter your age",min_value=1,max_value=100)

if name:
    st.write("Your name is:",name)
    st.write("Your age is:",age)

st.subheader("Sample Data")
st.table({
    "Name":["A","B"],
    "Marks":[85,90]
})

st.code("print('Hello, Streamlit!')",language="python")
st.divider()
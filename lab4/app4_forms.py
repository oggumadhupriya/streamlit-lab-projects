import streamlit as st

st.title("Forms and Session State")
st.write("Enter your details and submit the form.")

if "submissions" not in st.session_state:
    st.session_state.submissions=0

with st.form("student_form"):
    name=st.text_input("Student Name")

    course=st.selectbox(
        "Select Course",
        ["Python","Data Science","Web Technology"]
    )

    marks=st.number_input(
        "Enter Marks",
        min_value=0,
        max_value=100,
        value=75
    )

    submitted=st.form_submit_button("Submit Form")

if submitted:
    if name.strip():
        st.session_state.submissions+=1
        st.success("Form submitted successfully!")
        st.write("Student Name:",name)
        st.write("Course:",course)
        st.write("Marks:",marks)
        st.write("Total submissions:",st.session_state.submissions)
    else:
        st.warning("Please enter your name.")

st.divider()
st.subheader("Session State")
st.write(
    "Session state remembers values during app reruns "
    "within your current session."
)
st.write("Successful submissions:",st.session_state.submissions)

import streamlit as st
import pandas as pd

from db import (
    init_db,
    create_user,
    get_user_by_username,
    get_all_users,
    user_exists
)

from auth import (
    hash_password,
    verify_password,
    validate_username,
    validate_email,
    validate_password
)


st.set_page_config(
    page_title="Login and Signup App",
    page_icon="🔐",
    layout="centered"
)

@st.cache_resource
def setup_database():
    init_db()
    return True

try:
    setup_database()
except Exception as e:
    st.error("Could not connect to PostgreSQL.")
    st.error("Check your database settings in .streamlit/secrets.toml.")
    st.stop()

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if "user" not in st.session_state:
    st.session_state.user=None


st.title("🔐 User Authentication System")

def signup_page():
    st.subheader("Create an Account")

    with st.form("signup_form"):
        username=st.text_input("Username")
        email=st.text_input("Email")
        password=st.text_input("Password", type="password")
        confirm_password=st.text_input(
            "Confirm Password",
            type="password"
        )

        submitted=st.form_submit_button(
            "Sign Up",
            use_container_width=True
        )

    if submitted:
        username=username.strip()
        email=email.strip()

        valid,message=validate_username(username)
        if not valid:
            st.error(message)
            return

        valid,message=validate_email(email)
        if not valid:
            st.error(message)
            return

        valid,message=validate_password(password)
        if not valid:
            st.error(message)
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        if user_exists(username=username):
            st.error("That username already exists.")
            return

        if user_exists(email=email):
            st.error("That email is already registered.")
            return

        success=create_user(
            username,
            email,
            hash_password(password)
        )

        if success:
            st.success("Account created successfully! Please log in.")
        else:
            st.error("Could not create account. Try another username or email.")


def login_page():
    st.subheader("Login")

    with st.form("login_form"):
        username=st.text_input("Username")
        password=st.text_input("Password",type="password")

        submitted=st.form_submit_button(
            "Login",
            use_container_width=True
        )

    if submitted:
        user=get_user_by_username(username.strip())

        if user and verify_password(
            password,
            user["password_hash"]
        ):
            st.session_state.logged_in=True
            st.session_state.user=user
            st.rerun()
        else:
            st.error("Invalid username or password.")


def dashboard_page():
    user=st.session_state.user

    st.success(f"Welcome,{user['username']}!")

    col1, col2 = st.columns(2)
    col1.metric("User ID",user["id"])
    col2.metric("Username",user["username"])

    st.write("**Email:**",user["email"])
    st.write("**Account created:**",user["created_at"])

    st.divider()
    st.subheader("Registered Users")

    users=get_all_users()

    if users:
        df=pd.DataFrame(users)
        st.dataframe(df,use_container_width=True)
    else:
        st.info("No registered users found.")

    if st.button("Logout",use_container_width=True):
        st.session_state.logged_in=False
        st.session_state.user=None
        st.rerun()

if st.session_state.logged_in:
    dashboard_page()
else:
    login_tab,signup_tab=st.tabs(["Login","Sign Up"])

    with login_tab:
        login_page()

    with signup_tab:
        signup_page()
import streamlit as st
import requests
import time

st.set_page_config(page_title="Weather API Demo", layout="wide")

st.title("🌤️ Weather API Demo")
st.write("Explore weather data displayed in JSON format.")

API_KEY = "demo_key"

city=st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city name.")
    else:
        try:
            with st.spinner("Fetching weather..."):
 
                time.sleep(1)

                resp={
                    "city":city.strip(),
                    "temperature":30,
                    "condition":"Sunny",
                    "humidity":65
                }

            st.subheader("Weather Response (JSON)")
            st.json(resp)

            c1,c2,c3=st.columns(3)

            c1.metric("Temperature",f"{resp['temperature']}°C")
            c2.metric("Condition",resp["condition"])
            c3.metric("Humidity",f"{resp['humidity']}%")

        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again.")
        except requests.exceptions.RequestException as e:
            st.error(f"Request error:{e}")
        except Exception as e:
            st.error(f"Something went wrong:{e}")

st.markdown("---")
st.subheader("HTTP Methods")

st.markdown("""
- **GET** — Retrieve data
- **POST** — Send data
- **PUT** — Update data
- **DELETE** — Delete data
""")

st.info(
    "This lab uses simulated weather data. "
    "The temperature and humidity are examples, not live measurements."
)

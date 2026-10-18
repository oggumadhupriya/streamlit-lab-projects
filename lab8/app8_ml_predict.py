import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Iris Prediction",layout="wide")
st.title("Iris Flower Prediction")
st.write("Adjust the flower measurements and click Predict.")

model=joblib.load("model.pkl")
classes=["Setosa","Versicolor","Virginica"]

if "history" not in st.session_state:
    st.session_state.history=[]

with st.form("prediction_form"):
    sl=st.slider("Sepal Length (cm)",4.0,8.0,5.1)
    sw=st.slider("Sepal Width (cm)",2.0,4.5,3.5)
    pl=st.slider("Petal Length (cm)",1.0,7.0,1.4)
    pw=st.slider("Petal Width (cm)",0.1,2.5,0.2)

    submit=st.form_submit_button("Predict")

if submit:
    features=np.array([[sl,sw,pl,pw]])

    pred=model.predict(features)[0]
    proba=model.predict_proba(features)[0]

    st.success(f"Prediction:**{classes[pred]}**")
    st.metric("Confidence",f"{max(proba)*100:.1f}%")

    st.subheader("Class Probabilities")
    proba_df=pd.DataFrame({
        "Class":classes,
        "Probability":proba
    })
    st.bar_chart(proba_df.set_index("Class"))

    st.session_state.history.append({
        "Sepal Length":sl,
        "Sepal Width":sw,
        "Petal Length":pl,
        "Petal Width":pw,
        "Prediction":classes[pred]
    })

st.subheader("Prediction History")

if st.session_state.history:
    st.dataframe(pd.DataFrame(st.session_state.history))
else:
    st.info("Your predictions will appear here after you click Predict.")
import streamlit as st
import pandas as pd

st.title("Upload CSV and Analyze")

file=st.file_uploader("Upload a CSV file",type=["csv"])

if file is not None:
    df=pd.read_csv(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Filter by Column")
    col=st.selectbox("Choose column",df.columns)
    value=st.text_input("Filter value")

    if value:
        filtered=df[
            df[col].astype(str).str.contains(
                value,case=False,na=False
            )
        ]
        st.dataframe(filtered)

    st.subheader("Sort")
    sort_col=st.selectbox(
        "Sort by",df.columns,key="sort"
    )
    st.dataframe(df.sort_values(sort_col))

    csv=df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="processed.csv",
        mime="text/csv"
    )

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    option = st.radio(
        "Handle missing values:",
        ["Keep", "Drop", "Fill with 0"]
    )

    if option=="Drop":
        cleaned_df=df.dropna()
    elif option=="Fill with 0":
        cleaned_df=df.fillna(0)
    else:
        cleaned_df=df.copy()

    st.dataframe(cleaned_df)

    st.subheader("Group By and Average")

    group_col = st.selectbox(
        "Group by", df.columns, key="group"
    )

    num_cols=df.select_dtypes(
        include="number"
    ).columns

    if len(num_cols)>0:
        agg=df.groupby(group_col)[list(num_cols)].mean()
        st.dataframe(agg)
    else:
        st.info("No numeric columns are available.")

else:
    st.info("Please upload a CSV file to begin.")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard",layout="wide")
st.title("Sales Dashboard")

df=pd.DataFrame({
    "Year":np.random.choice([2022,2023,2024],200),
    "Region":np.random.choice(
        ["North","South","East","West"],200
    ),
    "Product":np.random.choice(["A","B","C"],200),
    "Sales":np.random.randint(1000,10000,200)
})

df["Date"]=pd.date_range(
    "2022-01-01",periods=200,freq="D"
)

st.sidebar.header("Filters")

year=st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

region=st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

product=st.sidebar.multiselect(
    "Product",
    sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

date_range=st.sidebar.date_input(
    "Date range",
    value=(df["Date"].min().date(),df["Date"].max().date())
)

filtered = df[
    df["Year"].isin(year)
    & df["Region"].isin(region)
    & df["Product"].isin(product)
]

if len(date_range)==2:
    filtered=filtered[
        (filtered["Date"]>=pd.Timestamp(date_range[0]))
        & (filtered["Date"]<=pd.Timestamp(date_range[1]))
    ]

c1,c2,c3=st.columns(3)

c1.metric("Total Sales",f"{filtered['Sales'].sum():,}")
avg_sales = filtered["Sales"].mean()
c2.metric("Avg Sales", f"{avg_sales:,.0f}"if not filtered.empty else "0")
c3.metric("Records",len(filtered))

if filtered.empty:
    st.warning("No records match the selected filters.")
else:
    st.subheader("Sales by Region")
    region_sales=filtered.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

    st.subheader("Sales by Year")
    year_sales=filtered.groupby("Year")["Sales"].sum()
    st.line_chart(year_sales)

    st.subheader("Sales by Product")
    pie_data=(
        filtered.groupby("Product")["Sales"]
        .sum()
        .reset_index()
    )
    fig=px.pie(
        pie_data,
        names="Product",
        values="Sales",
        title="Sales by Product"
    )
    st.plotly_chart(fig,use_container_width=True)

csv=filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered CSV",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)
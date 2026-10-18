import streamlit as st

st.title("Layouts Demo")
st.write("Learn how to organize a Streamlit app.")

st.sidebar.header("Settings")

theme=st.sidebar.selectbox(
    "Choose Theme",
    ["Light","Dark"]
)

font_size=st.sidebar.slider(
    "Font Size",
    10,30,15
)

st.sidebar.write("Selected theme:", theme)
st.sidebar.write("Font size:", font_size)

st.subheader("Dashboard Metrics")

col1,col2=st.columns(2)

with col1:
    st.metric("Total Sales", "25 Lakh")

with col2:
    st.metric("Customers", "1,200")

tab1, tab2, tab3 = st.tabs(
    ["Overview", "Analysis", "About"]
)

with tab1:
    st.header("Overview")
    st.write("This section displays an overview of the app.")

with tab2:
    st.header("Analysis")
    st.write("This section displays sales and customer analysis.")

with tab3:
    st.header("About")
    st.write("This app demonstrates Streamlit layouts.")

with st.container():
    st.subheader("Grouped Section")
    st.write("These elements are inside one container.")

with st.expander("View More Details"):
    st.write("This content appears when you expand this section.")
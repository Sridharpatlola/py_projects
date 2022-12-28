import streamlit as st
import plotly.express as px
import pandas as pd

from streamlit_option_menu import option_menu

st.set_page_config('Sridhar',"✌","wide")
st.markdown("<h1 style='text-align:center;color:blue;background-color:cyan;'>My Python Apps</h1>",unsafe_allow_html=True)
options = option_menu(menu_title="", options=["Simple Interest calculator","Sales dashboard"], orientation="horizontal")
if options == "Simple Interest calculator":
    st.title("Simple interest calculator")
    P = st.number_input("Enter the principal amount")
    T = st.number_input("Enter the time in years")
    R = st.number_input("Enter the rate of interest")
    I = (P * T * R) / 100
    if st.button("Calculate interest"):
        st.success("The simple interest is {}".format(I))
if options == "Sales dashboard":
    # st.warning("App is in progress")
    df = pd.read_csv("D:\supermarket_sales.csv")
    fig1= px.pie(df, 'City', 'gross income')
    fig2 = px.pie(df, 'Product line', 'gross income')
    cols=st.columns(2)
    cols[0].markdown("Income share by city")
    cols[0].plotly_chart(fig1,use_container_width=True)
    cols[1].markdown("Income share by product line")
    cols[1].plotly_chart(fig2,use_container_width=True)







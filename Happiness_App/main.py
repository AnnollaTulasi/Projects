import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search For Happiness")
x_axis = st.selectbox("Select the data for the X-Axis",("GDP","Happiness","Generosity"))
y_axis = st.selectbox("Select the data for the Y-Axis",("GDP","Happiness","Generosity"))

df = pd.read_csv("happy.csv")

match x_axis:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]
st.subheader(f"{x_axis} and {y_axis}")

figure= px.scatter(x=x_array, y=y_array, labels={"x":f"{x_axis}", "y": f"{y_axis}"})
st.plotly_chart(figure)



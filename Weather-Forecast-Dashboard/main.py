import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view ", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")

data = get_data(place, days, option)

dates = ["2026-21-06","2026-22-06","2026-23-06"]
temperatures = [10, 11, 15]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures (C)"})
st.plotly_chart(figure)
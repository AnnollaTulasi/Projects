import requests
import streamlit as st

api_key = "CizQFfU8OpWNsyR8OpUuE6wUQQXn6qYdVtrtxOyI"
url = "https://api.nasa.gov/planetary/apod?"\
    f"api_key={api_key}"

response = requests.get(url)
data = response.json()
print(data)

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
image_response = requests.get(image_url)
with open(image_filepath,"wb") as file:
    file.write(image_response.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
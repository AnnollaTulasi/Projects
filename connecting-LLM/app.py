import requests
from send_email import send_email
from langchain.chat_models import init_chat_model

api_key = "6e7f4ef989d1456f977963dce9abbde0"
GEMINI_API_KEY = "AQ.Ab8RN6Ix2PvWc75-3Z782b7UyQvmLyYY331Ek_t8bGkjEvBJNA"

url = (
    "https://newsapi.org/v2//top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&apiKey=" + api_key
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
articles = content["articles"]

# AI summarizing the news
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=GEMINI_API_KEY,
)

prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news.
Add another second paragraph to tell me
how they affect the stock market.
Here are the news articles:
{articles}
"""

response = model.invoke(prompt)
response_str = response.content

body = "Subject: News Summary\n\n" + response_str + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
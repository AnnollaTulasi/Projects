import requests

from send_email import send_email

api_key = "6e7f4ef989d1456f977963dce9abbde0"
url =  "https://newsapi.org/v2/everything?q=tesla&from=2026-05-04&sortBy=publishedAt&apiKey=6e7f4ef989d1456f977963dce9abbde0"

request = requests.get(url)
content = request.json()
body = " "
for article in content["articles"]:
    body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"
print(body)
body = body.encode("utf-8")
send_email(body)
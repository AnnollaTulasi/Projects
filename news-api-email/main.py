import requests

from send_email import send_email

api_key = "6e7f4ef989d1456f977963dce9abbde0"
url =  "https://newsapi.org/v2/everything?"\
       "q=tesla&sortBy=publishedAt&apiKey=6e7f4ef989d1456f977963dce9abbde0&language=en"

request = requests.get(url)
content = request.json()
#print(content)
body = " "
for article in content["articles"][:20]:
    body = "Subject: Todays news" + "\n" + body + article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"
#print(body)
body = body.encode("utf-8")
send_email(body)
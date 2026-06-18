from flask import Flask,render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def temp(station,date):
    return {"station": station,
            "date": date,
            "temp": 0}

if __name__ == "__main__":
    app.run(debug=True)
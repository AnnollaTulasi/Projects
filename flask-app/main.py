from fileinput import filename
import pandas as pd
from flask import Flask,render_template

app = Flask(__name__)
station_details = pd.read_csv("data_small/stations.txt", skiprows=17)
station_details = station_details[["STAID","STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html",data=station_details.to_html())

@app.route("/api/v1/<station>/<date>")
def temp(station,date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temp": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    return df.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station,year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    return df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")

if __name__ == "__main__":
    app.run(debug=True)
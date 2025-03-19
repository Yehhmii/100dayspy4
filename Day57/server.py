from flask import Flask, render_template
import datetime
import requests
import json
import ast

app = Flask(__name__)


@app.route('/')
def home():
    date = datetime.datetime.now()
    year = date.year
    return render_template("index.html", date=year)


@app.route('/guess/<name>')
def guess(name):
    response_gender = requests.get(f"https://api.genderize.io?name={name}").json()
    response_age = requests.get(f"https://api.agify.io?name={name}&country_id=US").json()
    gender = response_gender["gender"]
    age = response_age["age"]
    return render_template("guess.html", gender=gender, age=age, name=name)

@app.route('/blog')
def blog_post():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    resp = requests.get(url)
    resp.raise_for_status()
    response = resp.json()
    print(response)
    return render_template("blog.html", blogs=response)

if __name__ == "__main__":
    app.run(debug=True)
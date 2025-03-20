from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
# print(response)

@app.route('/')
def home():
    return render_template("index.html", data=response)


@app.route('/blog/<int:num>')
def get_blog(num):
    for blog in response:
        if blog["id"] == num:
            requested = blog
            return render_template("post.html", blog=requested)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

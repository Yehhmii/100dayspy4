from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", data=response)


@app.route('/post/<int:ids>')
def get_post(ids):
    for post in response:
        if post["id"] == ids:
            blog_requested = post
            return render_template("post.html", blog=blog_requested)


if __name__ == "__main__":
    app.run(debug=True)

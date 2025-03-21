from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h2>Name: {name}, Password: {password}<h2>"

if __name__ == "__main__":
    app.run(debug=True)

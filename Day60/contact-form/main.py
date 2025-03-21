from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", success='Successfully sent your message')
    elif request.method == 'GET':
        return render_template("contact.html")


def send_email(uname, user_email, phone, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.ehlo()
        print(email, password)
        conn.login(user=email, password=password)
        conn.sendmail(from_addr=email, to_addrs=email, msg="Subject: New contact \n\n "
                                                           f"Name: {uname} \n"
                                                           f"Email: {user_email} \n"
                                                           f"Phone: {phone} \n"
                                                           f"Message: {message}")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

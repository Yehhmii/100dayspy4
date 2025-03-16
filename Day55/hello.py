from flask import Flask

app = Flask(__name__)

def bold_decorator(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@app.route('/')
def hello():
    return ('<h2 style="text-align:center">Hello there!</h2>'
            '<p>are u from around here</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnkxMTVhcXgzcWM5dDg3NmR1aHE3cWQzd3pxMXlmMTg3ZjVubGJ4NiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/SS40oFiyppsHhvClo2/giphy.gif">')


@app.route('/bye')
@bold_decorator
def bye():
    return "Bye for now"

@app.route('/username/<name>')
def greeting(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)

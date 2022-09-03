#!/usr/bin/python3
"""
A minimal application exaple using flask
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_word():
    """
    displays Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_word2():
    """
    displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    displays display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    parsed_text = escape(text.replace('_', ' '))
    return f'C {parsed_text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

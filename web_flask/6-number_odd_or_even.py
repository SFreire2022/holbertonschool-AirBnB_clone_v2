#!/usr/bin/python3
"""
A minimal application exaple using flask
"""
from flask import Flask
from markupsafe import escape
from flask import render_template


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
    return 'C {}'.format(parsed_text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    parsed_text = escape(text.replace('_', ' '))
    return 'Python {}'.format(parsed_text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return '{} is a number'.format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_a_number_template(n):
    """
    display a HTML page only if n is an integer:
    h1 tag: “Number: n” inside the tag body
    """
    return render_template('5-number.html', n=escape(n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

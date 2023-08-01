#!/usr/bin/python3
""" number- odd or even"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html',
                           number=n, is_even=is_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

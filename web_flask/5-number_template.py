#!/usr/bin/python3
"""Starts a web application"""
from flask import Flask,  render_template, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns C followed by the vallued of text"""
    new_text = escape(text).replace('_', ' ')
    return "C %s" % new_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    new_text = escape(text).replace('_', ' ')
    return "Python %s" % new_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>',  strict_slashes=False)
def number_templates(n):
    return render_template('5-number.html', n= n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

#!/usr/bin/python3
"""
This Flask application serves responses for three routes:
- Root path (/): returns "Hello HBNB!"
- /hbnb: returns "HBNB"
- /c/<text>: replaces underscores with spaces in the provided text and prepends "C ".

It adheres to PEP 8 style guidelines (version 1.7) and includes docstrings for the Flask application (`__doc__`) and functions (`hello_world`, `hbnb`, and `c_route`).
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    This function handles requests to the root path (/).

    Returns:
        str: The response string "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function handles requests to the /hbnb path.

    Returns:
        str: The response string "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    This function handles requests to the /c/<text> path.
    It replaces underscores in the provided text with spaces and prepends "C ".

    Args:
        text (str): The text passed in the URL after /c/.

    Returns:
        str: modified text with underscores replaced by spaces and "C " .
    """
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
This Flask application serves responses for five routes:
- Root path (/): returns "Hello HBNB!"
- /hbnb: returns "HBNB"
- /c/<text>: replaces underscores with spaces and prepends "C ".
- /python/<text> (with default): 
  - If no text is provided, defaults to "is cool" and returns "Python is cool".
  - If text is provided, replaces underscores with spaces and prepends "Python ".
- /number/<int:n>: validates the provided argument as an integer
- returns a message indicating it's a number.
"""

from flask import Flask
import re  # Assuming this import is not used

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    Returns a string "Hello HBNB!" as a response to the root path (/).
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a string "HBNB" as a response to the /hbnb path.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Replaces underscores in the provided text with spaces and prepends "C ".

    Args:
        text: The text passed in the URL after /c/.

    Returns:
        The modified text with underscores replaced by spaces and "C " prepended.
    """
    return "C " + text.replace("_", " ")

@app.route('/python/<text>', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    This function handles requests to the /python/<text> route. 
    """
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Validates the provided argument as an integer 
    and returns a message indicating it's a number.

    Args:
        n: The integer passed in the URL after /number/.

    Returns:
        str: A message indicating n is a number.
    """
    return str(n) + " is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

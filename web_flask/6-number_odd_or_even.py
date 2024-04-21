#!/usr/bin/python3
"""
This Flask application serves responses for routes demonstrating:
- Static content: Root path (/).
- Text responses: /hbnb, /c/<text>, /python/<text>, /number/<int:n>.
- Templated responses: /number_template/<int:n>, /number_odd_or_even/<int:n>.

The application uses render_template to display template files
for number display and odd/even checking.
"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    This function returns a string "Hello HBNB!" as a response to the root path (/).
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string "HBNB" as a response to the /hbnb path.
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
    This function validates the provided argument as an integer and
    returns a message indicating it's a number.

    Args:
        n: The integer passed in the URL after /number/.

    Returns:
        str: A message indicating n is a number.
    """
    return str(n) + " is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function renders the 6-number.html template with the provided integer n.

    Args:
        n: The integer passed in the URL after /number_template/.

    Returns:
        The rendered template content.
    """
    return render_template('6-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    This function checks if the provided number is even or odd and
    renders the 6-number_odd_or_even.html template.

    Args:
        n: The integer passed in the URL after /number_odd_or_even/.

    Returns:
        The rendered template content.
    """
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


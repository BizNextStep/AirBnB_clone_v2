#!/usr/bin/python3
"""
This Flask application serves a simple response "Hello HBNB!" on the root path (/).

It demonstrates the following:
- Flask application creation using Flask class.
- Route definition using the @app.route decorator.
- Function to handle the request and return the response.
- Running the development server on all network interfaces 
- (host='0.0.0.0') and port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles requests to the root path (/).

    Returns:
        str: The response string "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

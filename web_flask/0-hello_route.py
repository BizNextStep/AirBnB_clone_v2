#!/usr/bin/python3
"""
This Flask application serves a simple "Hello HBNB!" message on the root path (/).
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    This function returns a string "Hello HBNB!" as a response to the root path (/).
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

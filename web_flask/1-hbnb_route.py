#!/usr/bin/python3
"""
This Flask application serves responses for two routes:
- Root path (/): returns "Hello HBNB!"
- /hbnb: returns "HBNB"
"""

from flask import Flask

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
    This function returns a string "HBNB" as a response to the /hbnb path.
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
Flask application to display a list of states from the storage engine.

Uses DBStorage and requires a running MySQL database with
HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, and HBNB_MYSQL_DB
environment variables set.

- Adheres to PEP 8 style guidelines (version 1.7).
- Includes docstrings for the Flask application (`__doc__`)
- and functions (`states_list`, `teardown_db`).
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Retrieves all State objects from storage, sorts them by name,
    and renders the 7-states_list.html template with the list.
    """
    states = storage.all("State").values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

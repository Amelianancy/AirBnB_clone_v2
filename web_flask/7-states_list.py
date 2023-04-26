#!/usr/bin/python3
"""A script that starts a web flask application
listens to 0.0.0.0:5000
"""


from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """closes the session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """renders the template 7-states_list.html"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

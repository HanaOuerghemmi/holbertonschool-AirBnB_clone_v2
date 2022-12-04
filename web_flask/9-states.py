#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=""):
    state = []
    data = storage.all(State)
    for key, value in data.items():
        state.append(value)
    if id:
        key = "State." + id
        if key not in data:
            state = ""

    cities = []
    dt = storage.all(City)
    for key, value in dt.items():
        cities.append(value)
    return render_template("9-states.html", id=id, state=state, cities=cities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

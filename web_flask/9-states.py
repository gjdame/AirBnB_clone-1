#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/states')
def display():
    return render_template('9-states.html', storage=storage.all('State'))

@app.route('/states/<id>')
def display_by_id():
    return render_template('9-states.html', storage=storage.all('State'))

@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

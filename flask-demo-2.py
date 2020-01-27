#!/usr/bin/env python3
from flask import Flask, jsonify # jsonfiy is like json but build into Flask, or something. 
app = Flask(__name__)

stuff = { 
        'people': ['John', 'Jacob', 'Jinklheimer', 'Smith', 'Bob'], 
        'places': ['Chicago', 'Los Vegas', 'New York', 'Hell'],
        'things': ['Pumkin', 'Spice', 'Puppies', 'Kittens', 'Weed'],
        }

@app.route('/') # Root Path
def root_path():
    return stuff

@app.route('/people')
def people_path():
    return jsonify(stuff['people']) # Needed to return lists

@app.route('/places')
def places_path():
    return jsonify(stuff['places'])

@app.route('/things')
def things_path():
    return jsonify(stuff['things'])

app.run()

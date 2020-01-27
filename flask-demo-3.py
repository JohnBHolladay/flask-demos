#!/usr/bin/env python3
from flask import Flask, jsonify # jsonfiy is like json but build into Flask, or something. 
app = Flask(__name__)

stuff = { 
        'people': ['John', 'Jacob', 'Jinklheimer', 'Smith', 'Bob'], 
        'places': ['Chicago', 'Los Vegas', 'New York', 'Hell'],
        'things': ['Pumkin', 'Spice', 'Puppies', 'Kittens', 'Weed'],
        }

@app.route('/', defaults={ 'lookup': None })
@app.route('/<string:lookup>')
def smarter_path(lookup):
    if lookup:
        return jsonify(stuff[lookup])
    return stuff

app.run()

#!/usr/bin/env python3
from flask import Flask, jsonify
from waitress import serve # Import waitress, to use instead of Flask's default webserver
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

serve(app) # This is the only thing that changed besides the import.
           # It seems to default to port 8080 instead of 5000. 
           # It may bitch about favicon.ico not being found. 
           # That's fine, favicon.ico is the little icon that shows up in your address bar when you go to a page.

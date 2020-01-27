#!/usr/bin/env python3
from flask import Flask, jsonify
from waitress import serve # Import waitress, to use instead of Flask's default webserver
app = Flask(__name__)

stuff = { 
        'people': ['John', 'Jacob', 'Jinklheimer', 'Smith', 'Bob'], 
        'places': ['Chicago', 'Los Vegas', 'New York', 'Hell'],
        'things': ['Pumkin', 'Spice', 'Puppies', 'Kittens', 'Weed'],
        }

# Just to shut it up... If this returned an icon it would show up in the address bar.
@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/', defaults={ 'lookup': None })
@app.route('/<string:lookup>')
def smarter_path(lookup):
    html = ['<h1>Stuff Looker Upper</h1>']
    if lookup:
        html.append(f"<ul>")
        for item in stuff[lookup]:
            html.append(f"<li>{item}</li>")
        html.append('</ul>')
    else:
        for group, items in stuff.items():
            html.append(f"<h2>{group}</h2>")
            html.append('<ul>')
            for item in items:
                html.append(f"<li>{item}</li>")
            html.append('</ul>')
    return ''.join(html)

serve(app) # This is the only thing that changed besides the import.
           # It seems to default to port 8080 instead of 5000. 
           # It may bitch about favicon.ico not being found. 
           # That's fine, favicon.ico is the little icon that shows up in your address bar when you go to a page.

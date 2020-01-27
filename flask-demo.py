#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/') # This is the root path. Can define another function at something like /anotherpage to return something else.
def some_function(): # Doesn't matter what this is called.
    return 'Hello, World!' # Can also be things other than a string, like a dictionary.

app.run()

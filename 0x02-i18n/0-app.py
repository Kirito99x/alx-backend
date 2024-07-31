#!/usr/bin/env python3
"""A basic Flask app.
This app serves as a starting point for a Flask web application.
"""
from flask import Flask, render_template



app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def get_index() -> str:
    """Returns the home/index page.
    This function renders the '0-index.html' template and returns it as a response.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

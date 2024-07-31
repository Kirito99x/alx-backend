#!/usr/bin/env python3
"""A Basic Flask app.
This script sets up a basic Flask application with internationalization support using Flask-Babel.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Represents the configuration for Flask Babel.
    This class defines the configuration options for Flask Babel, including the supported languages,
    default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The handler for the home/index page.
    This function renders the '1-index.html' template and returns the rendered HTML as a string.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

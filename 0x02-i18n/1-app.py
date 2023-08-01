#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Config class with available languages
class Config:
    """Config class with available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Instanti in a module-level variable named babel
babel = Babel(app)


@app.route('/')
def index():
    """A basic route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

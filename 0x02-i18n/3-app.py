#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)


# Config class with available languages
class Config:
    """Config class with available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Instantiatein a module-level variable named babel
babel = Babel(app)


@app.route('/')
def index():
    """A basic route"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """configure the language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()

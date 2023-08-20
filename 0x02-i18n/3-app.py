#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """app configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index():
    """home route"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """retruns supported languages"""
    supported_languages = app.config.get('LANGUAGES')
    return request.accept_languages.best_match(supported_languages)


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """app configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    return user dict or none if id non existent"""
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """executed b4 other ftns"""
    g.user = get_user()


@app.route("/")
def index():
    """home route"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """retruns supported languages"""
    supported_languages = app.config.get('LANGUAGES')
    # First, check if the locale is provided in URL parameters
    locale = request.args.get('locale')
    if locale and locale in supported_languages:
        return locale
    # Next, check if the user has a preferred locale in their settings
    user = getattr(g, 'user', None)
    if user and user.get('locale') and user['locale'] in supported_languages:
        return user['locale']
    # Then, check the request header for the preferred locale
    request_locale = request.headers.get("Accept-Language")
    if request_locale:
        request_locale = request_locale.split(',')[0].split(';')[0].lower()
        if request_locale in supported_languages:
            return request_locale
    # If no preferred locale is found, return the default locale (English)
    return 'en'


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
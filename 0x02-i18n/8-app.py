#!/usr/bin/env python3
"""builds on the previous ones and more"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, format_datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

global users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gives us a locale to translate the text to
    Returns:
        str: the best language
    """
    locale = request.args.get('locale')
    avail = app.config['LANGUAGES']
    if locale and locale in avail:
        return locale
    elif hasattr(g, 'user'):
        if g.user['locale'] in avail:
            return g.user['locale']
    else:
        locale = request.headers.get('Accept-Language')
        if locale in avail:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Tries to get a valid timzezone for us based
    on the user's preferences

    Returns:
        str: A valid timezone or UTC
    """
    tz = request.args.get('timezone')
    try:
        if tz:
            res = timezone(tz)
        elif hasattr(g, 'user'):
            tz = g.user['timezone']
            res = timezone(tz)
    except UnknownTimeZoneError:
        res = app.config['BABEL_DEFAULT_TIMEZONE']
    finally:
        return res


def get_user():
    """Tries to retrieve a user from our
    mock database

    Returns:
        dict: the user if found or None
    """
    id = request.args.get('login_as')
    user = None
    try:
        user = users.get(int(id), None)
    except (ValueError, TypeError):
        pass
    finally:
        return user


@app.before_request
def before_request():
    """To be called before thr request is
    processed to try and ascertain if the user if valid"""
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def index():
    """Returns our default page"""
    if hasattr(g, 'user'):
        username = g.user['name']
        tz = datetime.now()
        curr = format_datetime(tz, 'medium')
        logged_in = gettext('logged_in_as', username=username)
        ct = gettext('current_time_is', current_time=curr)
        return render_template('8-index.html', msg=True, logged_in=logged_in,
                               current_time_is=ct)
    return render_template('8-index.html', msg=False)


if __name__ == '__main__':
    app.run()

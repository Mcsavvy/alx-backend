#!/usr/bin/env python3
"""Creating our first translations
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """The configuration class for babel
    """
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Returns the default home page
    Returns:
        template: a html file
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()

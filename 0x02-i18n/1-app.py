#!/usr/bin/env python3
"""Configuring the app to use Babel
"""
from flask import Flask, render_template
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


@app.route('/')
def index():
    """Returns the default home page
    Returns:
        template: a html file
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

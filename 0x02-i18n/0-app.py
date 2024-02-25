#!/usr/bin/env python3
"""A minimalist flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Returns the default home page
    Returns:
        template: a html file
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

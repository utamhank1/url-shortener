from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h4234723n34h23n4293'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app

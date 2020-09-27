import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('FAHCLIENTSTATS_CONFIGFILE', silent=True)

    from . import status
    app.register_blueprint(status.bp)
    from . import clients
    app.register_blueprint(clients.bp)

    return app
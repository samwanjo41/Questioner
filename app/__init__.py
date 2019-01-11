"""Initialize app."""
import os
from flask import Flask
from .api.v1.views.user_view import method1

from config import app_config


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.register_blueprint(method1) 

    return app

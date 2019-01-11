"""Initialize app."""
import os
from flask import Flask

from config import app_config
from .api.v1.views.user_view import method1
from .api.v1.views.meetups_view import version2
from .api.v1.views.question_view import app1


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.register_blueprint(method1) 
    app.register_blueprint(version2) 
    app.register_blueprint(app1) 
    return app

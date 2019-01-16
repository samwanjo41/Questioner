"""Initialize app."""
import os
from flask import Flask

from config import app_config
from .api.v1.views.user_view import v1 as user_blueprint
from .api.v1.views.meetups_view import v1 as meetups_blueprint
from .api.v1.views.question_view import v1 as question_blueprint


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.register_blueprint(user_blueprint) 
    app.register_blueprint(meetups_blueprint) 
    app.register_blueprint(question_blueprint) 
    return app

"""
The app configurations
"""
import os

class Config:
    """
    The default configuration class
    """
    DEBUG = False
    SECRET = os.getenv('SECRET')
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """
    The development configuration class
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    The development configuration class
    """
    DEBUG = False
    TESTING = False



class TestingConfig(Config):
    """
    The testing configuration class
    """
    DEBUG = True
    TESTING = True


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig

}
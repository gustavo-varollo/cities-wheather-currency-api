import os
from flask import Flask
from config import Config


def create_app():
    """
    Core function that runs the application
    """
    app = Flask(__name__, instance_relative_config=True)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    from . import city_weather
    app.register_blueprint(city_weather.weather)
    from . import currency_exchange
    app.register_blueprint(currency_exchange.currency)
    return app


import os

from flask import Flask
from flask_assets import Environment
from project.conf import config, configfeatures

def create_app():
    from . import models, routes, compress, mail, redis, oauth

    app = Flask(__name__)
    flask_env = os.getenv('FLASK_ENV')
    #class ProductionConfig resides in folder project/conf/ and in file prod_config.py
    app.config.from_object(config[flask_env])
    config[flask_env].init_app(app) ##this is a class called ProductionConfig or DevelopmentConfig
    #config[flask_env] contatins the name of the class ProductionConfig or DevelopmentConfig init_app is a method in the class

    models.init_app(app)
    routes.init_app(app)
    mail.init_app(app)
    oauth.init_app(app)
    compress.init_app(app)
    redis.init_app(app)

    return app

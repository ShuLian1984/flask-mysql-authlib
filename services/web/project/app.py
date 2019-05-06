import os

from flask import Flask
from project.shared.database import db

#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from project.api.oauth2 import config_oauth

# instantiate the extensions
migrate = Migrate()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    #setup oauth2
    config_oauth(app)

    # register blueprints
    from project.api.main import main_blueprint
    app.register_blueprint(main_blueprint)
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.oauthroutes import oauthbp
    app.register_blueprint(oauthbp)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app

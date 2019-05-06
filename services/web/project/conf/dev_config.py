import os
from project.conf.configbase import ConfigBase
from dotenv import load_dotenv


class DevelopmentConfig(ConfigBase):

    @classmethod
    def init_app(cls, app):
        ConfigBase.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'
        flask_raygun.Provider(app, app.config['RAYGUN_APIKEY']).attach()

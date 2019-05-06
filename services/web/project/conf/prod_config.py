import os
from project.conf.configbase import ConfigBase, flask_raygun
from dotenv import load_dotenv


class ProductionConfig(ConfigBase):

    @classmethod
    def init_app(cls, app):
        ConfigBase.init_app(app)
        print('iiiiiiiiiiiiii', os.environ.get('RAYGUN_APIKEY') )
        for key, val in app.config.items():
            print("kkkkkkkkkkk ", key, val)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'
        #flask_raygun.Provider(app, app.config['RAYGUN_APIKEY']).attach()

import os
import sys
from dotenv import load_dotenv
from project.services import FileUtils
from raygun4py.middleware import flask as flask_raygun

APP_NAME = os.environ.get('APP_NAME') or 'Flask-Base'
PYTHON_VERSION = sys.version_info[0]
if PYTHON_VERSION == 3:
    import urllib.parse
else:
    import urlparse

class ConfigBase:
    basedir = os.path.abspath(os.path.dirname(__file__))

    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Analytics
    @staticmethod
    def init_googleanalytics(app):
        load_dotenv(ConfigBase.basedir + "googleanalytics.env")
        GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID') or ''
        SEGMENT_API_KEY = os.environ.get('SEGMENT_API_KEY') or ''

    @staticmethod
    def init_database(app):
        load_dotenv(ConfigBase.basedir + "db.env")
        MYSQL_DB = os.environ['MYSQL_DB']
        MYSQL_USER = os.environ['MYSQL_USER']
        MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
        MYSQL_HOST = os.environ['MYSQL_HOST'] #if used in container it should the n$
        MYSQL_PORT = os.environ['MYSQL_PORT']
        SQLALCHEMY_TRACK_MODIFICATIONS=False
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, 3306, MYSQL_DB
        )


    # Admin account
    @staticmethod
    def init_admin(app):
        load_dotenv(ConfigBase.basedir + "admin.env")
        ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'password'
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        ADMIN_EMAIL = os.environ.get(
            'ADMIN_EMAIL') or 'flask-base-admin@example.com'
        EMAIL_SUBJECT_PREFIX = '[{}]'.format(APP_NAME)
        EMAIL_SENDER = '{app_name} Admin <{email}>'.format(
            app_name=APP_NAME, email=MAIL_USERNAME)

    @staticmethod
    def init_mail(app):
        load_dotenv(ConfigBase.basedir + "mail.env")
        MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.sendgrid.net'
        MAIL_PORT = os.environ.get('MAIL_PORT') or 587
        MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
        MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
        MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
        RAYGUN_APIKEY = os.environ.get('RAYGUN_APIKEY')
        print('LoADING EMAIL env............', RAYGUN_APIKEY)


    # Parse the REDIS_URL to set RQ config variables
    @staticmethod
    def init_redis(app):
        load_dotenv(ConfigBase.basedir + "rq.env")
        REDIS_URL = os.getenv('REDISTOGO_URL') or 'http://localhost:6379'
        if PYTHON_VERSION == 3:
            urllib.parse.uses_netloc.append('redis')
            url = urllib.parse.urlparse(REDIS_URL)
        else:
            urlparse.uses_netloc.append('redis')
            url = urlparse.urlparse(REDIS_URL)
        RQ_DEFAULT_HOST = url.hostname
        RQ_DEFAULT_PORT = url.port
        RQ_DEFAULT_PASSWORD = url.password
        RQ_DEFAULT_DB = 0

    @staticmethod
    def init_app(app):
        ConfigBase.init_database(app)
        ConfigBase.init_googleanalytics(app)
        ConfigBase.init_mail(app)
        ConfigBase.init_admin(app)
        ConfigBase.init_redis(app)
        pass

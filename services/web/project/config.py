import os

USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')


#class ProductionConfig():
#    """Production configuration"""
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    SQLALCHEMY_DATABASE_URI = f'postgres://{USER}:{PASSWORD}@db:5432/users'
#
class ProductionConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    MYSQL_DB = os.environ['MYSQL_DB']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_HOST = os.environ['MYSQL_HOST'] #if used in container it should the name of the docker-compose service
    MYSQL_PORT = os.environ['MYSQL_PORT']
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, 3306, MYSQL_DB
    )

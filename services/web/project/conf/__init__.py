from project.conf.dev_config import DevelopmentConfig
from project.conf.prod_config import ProductionConfig

config = {
    'development': DevelopmentConfig,
    #'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    #'heroku': HerokuConfig,
    #'unix': UnixConfig
}

configfeatures = {
  'mail':True,
  'redis':True,
  'googleanalytics':True,
  'raygun':True
}

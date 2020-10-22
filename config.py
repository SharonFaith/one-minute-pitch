import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/one_min_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

#class TestConfig(Config):
 #   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/watchlist_test'

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
   
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
 #   'test': TestConfig
}
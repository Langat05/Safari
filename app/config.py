class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://langatj:Access@localhost/safari'
    SECRET_KEY = 'thisismysecretkeydonotstealit'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://langatj:Access@localhost/safari'

config_options = {
'development':DevConfig,
'production':ProdConfig
}
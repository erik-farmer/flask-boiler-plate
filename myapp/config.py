class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass

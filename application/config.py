import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite://:memory:')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

# Standard Lib
import logging
from logging.config import dictConfig
# Third Party
from flask import Flask
from werkzeug.utils import find_modules, import_string
# from raven.contrib.flask import Sentry
# App Specific
from application.utils.api_result import ApiResult, ApiException
from application.logging_config import LOGGING_CONFIG


class ApiFlask(Flask):
    def make_response(self, return_value):
        if isinstance(return_value, ApiResult):
            return return_value.to_response()
        return Flask.make_response(self, return_value)


def create_app(env):
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting application in env: {}'.format(env))
    app = ApiFlask(__name__)
    config = get_config(env)
    app.config.from_object(config)
    register_blueprints(app)
    register_error_handlers(app)
    register_extensions(app)

    return app


def get_config(env):
    return {
        'TEST': 'application.config.TestingConfig',
        'PROD': 'application.config.ProductionConfig'
    }.get(env, 'application.config.DevelopmentConfig')


def register_blueprints(app):
    for blueprint in find_modules('application.blueprints', include_packages=True):
        for filename in find_modules(blueprint):
            mod = import_string(filename)
            if hasattr(mod, 'bp'):
                app.register_blueprint(mod.bp)


def register_error_handlers(app):
    # Handle raising of an ApiException exception.
    app.register_error_handler(ApiException, lambda err: err.to_result())


def register_extensions(app):
    # Extensions can be set up like so:
    # sentry = Sentry(app, dsn=os.getenv('SENTRY_DSN'), logging=True, level=logging.ERROR)
    return app


def setup_logging():
    dictConfig(LOGGING_CONFIG)

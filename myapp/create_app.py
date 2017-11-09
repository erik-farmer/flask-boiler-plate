# Standard Lib
import logging
from logging.config import dictConfig
from logging_config import LOGGING_CONFIG
import os
# Third Party
from flask import Flask
from werkzeug.utils import find_modules, import_string
from raven.contrib.flask import Sentry
# App Specific
from api_result import ApiResult, ApiException


class ApiFlask(Flask):
    def make_response(self, return_value):
        if isinstance(return_value, ApiResult):
            return return_value.to_response()
        return Flask.make_response(self, return_value)


def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    register_blueprints(app)
    register_error_handlers(app)
    register_extensions(app)
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Starting application in env: {}'.format(app.config['env']))
    return app


def register_blueprints(app):
    for name in find_modules('myapp.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def register_error_handlers(app):
    # Handle raising of an ApiException exception.
    app.register_error_handler(ApiException, lambda err: err.to_result())
    # Catch all error handler.
    # TODO upgrade to function with logging and response.
    app.register_error_handler(500, lambda err: ('OH NOES!!!', 500))


def register_extensions(app):
    sentry = Sentry(app, dsn=os.getenv('SENTRY_DSN'), logging=True, level=logging.ERROR)
    return app

def setup_logging():
    dictConfig(LOGGING_CONFIG)

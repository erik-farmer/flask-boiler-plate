import logging
import os
from application.app_factory import create_app

app = create_app(os.getenv('ENV', 'DEV'))
logger = logging.getLogger(__name__)
"""
This is currently the best place for these functions I can think of. They CAN be put in the
'app_factory.register_error_handlers' call as a nested function BUT that makes it impossible to test.
"""


@app.errorhandler(Exception)
def catch_all_exception(exception):
    logger.exception(exception)
    return 'OH NOES!', 500

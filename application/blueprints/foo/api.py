# Standard Library
import logging
# Third Party
from flask import Blueprint
from flask.views import MethodView
# Module Specific
from application.utils.api_result import ApiResult
from application.utils.blueprint_utils import register_api

logger = logging.getLogger(__name__)
bp = Blueprint('foo', __name__, url_prefix='/foo')


class FooApi(MethodView):
    @staticmethod
    def get():
        logger.info('Oh Hi there')
        return ApiResult({'status': 'SUCCESS'})


foo_view = FooApi.as_view('foo_api')
register_api(foo_view, '/', bp)

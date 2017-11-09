import logging

from flask import Blueprint, request
from myapp.api_result import ApiResult, ApiException

bp = Blueprint('demo', __name__)

logger = logging.getLogger(__name__)


@bp.route('/add')
def add_numbers():
    logger.info('WE ABOUT TO ADD')
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


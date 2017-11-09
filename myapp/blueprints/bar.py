import logging
from flask import Blueprint, request
from myapp.api_result import ApiResult, ApiException
from flask import g
from random import random

bp = Blueprint('demo', __name__)

logger = logging.getLogger(__name__)


@bp.route('/add')
def add_numbers():
    logger.info('WE ABOUT TO ADD')
    someSetterWare()
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    someMiddleWare()
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


def someSetterWare():
    if g.get('eriksFunVar'):
        logger.info('already exists')
    else:
        g.eriksFunVar = random()


def someMiddleWare():
    if g.get('eriksFunVar'):
        logger.info(g.eriksFunVar)
    else:
        logger.info('OH NOES')

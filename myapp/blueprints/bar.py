from flask import Blueprint, request
from myapp.api_result import ApiResult, ApiException
from flask import g
from random import random

bp = Blueprint('demo', __name__)

@bp.route('/add')
def add_numbers():
    someSetterWare()
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    someMiddleWare()
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'sum': a + b})


def someSetterWare():
    if g.get('eriksFunVar'):
        print('already exists')
    else:
        g.eriksFunVar = random()


def someMiddleWare():
    if g.get('eriksFunVar'):
        print(g.eriksFunVar)
    else:
        print('OH NOES')
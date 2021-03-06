import logging
from flask import json, Response

logger = logging.getLogger(__name__)


class ApiResult(object):
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value), status=self.status, mimetype='application/json')


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        logger.exception(self.message)
        return ApiResult({'message': self.message}, status=self.status)

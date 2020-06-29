# coding=utf-8
import logging

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback
from rest_framework_simplejwt.exceptions import InvalidToken


_logger = logging.getLogger('api')


def api_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code

    if isinstance(exc, Exception):
        set_rollback()
        _logger.exception(repr(exc))
        if isinstance(exc, ValidationError):
            return Response({'msg': repr(exc), 'code': 400}, status=400)
        elif isinstance(exc, InvalidToken):
            return Response({'msg': repr(exc), 'code': 401}, status=401)

        return Response({'msg': 'Internal Server Error. Please contact to Admin!', 'code': 500}, status=500)

    return response

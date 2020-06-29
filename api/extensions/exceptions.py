# coding=utf-8
import logging

from rest_framework import status
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
            return wrap_response(repr(exc), status.HTTP_400_BAD_REQUEST)
        elif isinstance(exc, InvalidToken):
            return wrap_response(repr(exc), status.HTTP_401_UNAUTHORIZED)

        return wrap_response("Internal Server Error. Please contact to Admin!", status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response


def wrap_response(message, code):
    return Response({
        "message": message,
        "code": code,
    }, status=code)

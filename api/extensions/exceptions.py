# coding=utf-8
import logging

from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback


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
        return Response({'msg': 'Internal Server Error. Please contact to Admin!'}, status=500)

    return response

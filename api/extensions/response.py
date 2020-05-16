from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class HttpResponse(Response):
    def __init__(self, data=None, status=None, message=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        res_body = {}
        if data:
            res_body['data'] = data
        res_body['msg'] = message or 'OK'

        if status:
            code = status
        elif exception:
            code = HTTP_400_BAD_REQUEST
        else:
            code = HTTP_200_OK
        res_body['code'] = code

        content_type = content_type or 'application/json'
        super().__init__(res_body, status, template_name, headers, exception, content_type)

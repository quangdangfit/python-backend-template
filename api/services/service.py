# coding=utf-8
import logging

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.extensions.response import HttpResponse


_logger = logging.getLogger('api')


class CommonAPIView(APIView):
    """
        Common API View to handle request
    """
    repository = None
    serializer = None

    def serialize(self, records):
        many = True if (isinstance(records, QuerySet)) else False
        return self.serializer(records, many=many).data


class CommonView(CommonAPIView):
    """
        View to list all records of model in the system.
    """
    http_method_names = ['get', 'post']
    fields_filter = []

    def get(self, request, format=None):
        """
        Return a list of all record.
        """
        query = {field: request.query_params.get(field) for field in self.fields_filter}
        result = self.repository.list(query=query)
        return Response(self.serialize(result))

    def post(self, request, format=None):
        """
        Create and Return one record.
        """
        data = request.data
        result = self.repository.create(data)
        return Response(self.serialize(result))


class CommonSingleView(CommonAPIView):
    """
        View to get a record of model in the system.
    """
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, record_id=None, format=None):
        """
        Return single record.
        """
        result = self.repository.retrieve(record_id)
        if not result:
            return HttpResponse(message='Not found', status=status.HTTP_404_NOT_FOUND)

        return HttpResponse(data=self.serialize(result), status=status.HTTP_200_OK)

    def put(self, request, record_id, format=None):
        """
        Return single record.
        """
        data = request.data
        result = self.repository.update(record_id, data)

        if result:
            status_code = status.HTTP_200_OK
            msg = 'Update Success'
        elif result is False:
            status_code = status.HTTP_404_NOT_FOUND
            msg = 'Not Found'
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = 'Update Failed'

        return HttpResponse(message=msg, status=status_code)

    def delete(self, request, record_id, format=None):
        """
        Return single record.
        """
        result = self.repository.delete(record_id)
        if result:
            status_code = status.HTTP_200_OK
            msg = 'Delete Success'
        elif result is False:
            status_code = status.HTTP_404_NOT_FOUND
            msg = 'Not Found'
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            msg = 'Delete Failed'

        return HttpResponse(message=msg, status=status_code)

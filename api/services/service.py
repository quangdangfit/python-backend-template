# coding=utf-8
import logging

from django.db.models import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response

_logger = logging.getLogger('api')


class CommonAPIView(APIView):
    """
        Common API View to handle request
    """
    repository = None
    serializer = None

    def serialize(self, records):
        many = True if (isinstance(records, QuerySet) and records.count() > 1) else False
        return self.serializer(records, many=many).data


class CommonView(CommonAPIView):
    """
        View to list all records of model in the system.
    """
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        """
        Return a list of all record.
        """
        result = self.repository.list()
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
        return Response(result)

    def put(self, request, record_id, format=None):
        """
        Return single record.
        """
        data = request.data
        result = self.repository.update(record_id, data)
        return Response(result)

    def delete(self, request, record_id, format=None):
        """
        Return single record.
        """
        result = self.repository.delete(record_id)
        return Response(result)

# coding=utf-8
import logging

from django.core.exceptions import ObjectDoesNotExist


_logger = logging.getLogger('api')


class Repository:
    _name = 'repository'
    _model = None

    @classmethod
    def create(cls, data, *args, **kwargs):
        """
        Apply for POST method
        :param dict|list data:
        :param args:
        :param kwargs:
        :return:
        """
        result = cls._model.objects.create(**data)
        return result

    @classmethod
    def list(cls, *args, **kwargs):
        """
        Apply for GET method
        :param dict|list query:
        :param args:
        :param kwargs:
        :return:
        """
        query = kwargs.get('query', {})
        result = cls._model.objects.filter(**query)

        return result

    @classmethod
    def retrieve(cls, record_id, *args, **kwargs):
        """
        Apply for GET one item method
        :param record_id:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            result = cls._model.objects.get(id=record_id)
        except ObjectDoesNotExist:
            result = None

        return result

    @classmethod
    def update(cls, record_id, data, *args, **kwargs):
        """
        Apply for PUT method
        :param record_id:
        :param dict|list data:
        :param args:
        :param kwargs:
        :return:
        """
        record = cls._model.objects.all().filter(id=record_id)
        if not record:
            return False

        return record.update(**data)

    @classmethod
    def delete(cls, record_id, *args, **kwargs):
        """
        Apply DELETE method
        :param record_id:
        :param args:
        :param kwargs:
        :return:
        """
        record = cls._model.objects.all().filter(id=record_id)
        if not record:
            return False

        return record.delete()

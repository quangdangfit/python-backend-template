# coding=utf-8
import logging


_logger = logging.getLogger('api')


class Repository:
    _name = 'repository'
    _model = None

    @classmethod
    def create(self, data, *args, **kwargs):
        """
        Apply for POST method
        :param dict|list data:
        :param args:
        :param kwargs:
        :return:
        """
        result = self._model.objects.create(**data)
        return result

    @classmethod
    def list(self, query=None, *args, **kwargs):
        """
        Apply for GET method
        :param dict|list query:
        :param args:
        :param kwargs:
        :return:
        """
        result = self._model.objects.all()
        return result

    @classmethod
    def retrieve(self, record_id, *args, **kwargs):
        """
        Apply for GET one item method
        :param record_id:
        :param args:
        :param kwargs:
        :return:
        """
        return self._model.objects.get_or_404(id=record_id)

    @classmethod
    def update(self, record_id, data, *args, **kwargs):
        """
        Apply for PUT method
        :param record_id:
        :param dict|list data:
        :param args:
        :param kwargs:
        :return:
        """
        record = self._model.objects.get(id=record_id)
        return record.update(**data)

    @classmethod
    def destroy(self, record_id, *args, **kwargs):
        """
        Apply DELETE method
        :param record_id:
        :param args:
        :param kwargs:
        :return:
        """
        return self._model.objects.get(id=record_id)

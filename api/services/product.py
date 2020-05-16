# coding=utf-8
import logging

from api.repositories.product import ProductRepository
from api.serializers.product import ProductSerializer
from api.services.service import CommonView, CommonSingleView


_logger = logging.getLogger('api')


class ProductView(CommonView):
    """
        View to list all products or create product in the system.
    """
    repository = ProductRepository
    serializer = ProductSerializer


class ProductSingleView(CommonSingleView):
    """
        View to get/put/delete one product in the system.
    """
    repository = ProductRepository
    serializer = ProductSerializer

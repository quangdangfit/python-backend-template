# coding=utf-8
import logging

from api.models.product import Product
from api.repositories.repository import Repository


_logger = logging.getLogger('api')


class ProductRepository(Repository):
    _name = 'product_repository'
    _model = Product

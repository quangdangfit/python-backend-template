# coding=utf-8
import logging

from django.db import models

_logger = logging.getLogger('api')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'product'

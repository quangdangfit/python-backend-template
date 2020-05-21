# coding=utf-8
import logging

from django.db import models


_logger = logging.getLogger('api')


# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=15, unique=True, null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'product'

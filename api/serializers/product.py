# coding=utf-8
from rest_framework import serializers

from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['code', 'name']

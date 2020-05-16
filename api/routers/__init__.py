# coding=utf-8

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.services.product import ProductView, ProductSingleView


urlpatterns = [
    path('products', ProductView.as_view()),
    path('products/<int:record_id>', ProductSingleView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

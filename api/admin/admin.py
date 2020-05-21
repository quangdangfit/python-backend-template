from django.contrib import admin
from api.models.product import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    ordering = ['-id']
    search_fields = ['name', 'description']

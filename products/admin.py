from django.contrib import admin
from django.utils.text import Truncator

from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','short_description','price', 'status', 'created_at']
    list_filter = ['status','created_at']
    search_fields = ['title']

    
    def short_description(self,obj):
        return Truncator(obj.description).words(5)
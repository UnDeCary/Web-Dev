from django.contrib import admin
from .views import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "price", "count", "is_active", "category")
    list_filter = ("is_active", "category", "price")
    search_fields = ("name", "description")
    list_editable = ('is_active', 'price', 'count')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
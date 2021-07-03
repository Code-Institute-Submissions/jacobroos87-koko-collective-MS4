from django.contrib import admin
from .models import Product, Category, ProductImages

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

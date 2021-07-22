from django.contrib import admin
from .models import Product, Category, ProductImage

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'avg_rating',
        'is_featured',
        ProductImage,
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

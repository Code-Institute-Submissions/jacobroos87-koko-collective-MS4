from django.contrib import admin
from .models import Wishlist

# Register your models here.

class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist
    list_display = (
        "user",
    )

admin.site.register(Wishlist, WishlistAdmin)

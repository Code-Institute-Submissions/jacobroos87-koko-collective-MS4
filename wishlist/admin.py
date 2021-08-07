from django.contrib import admin
from .models import Wishlist

# Register your models here.
# adds the user to the wishlist information
class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist
    list_display = (
        "user",
    )

admin.site.register(Wishlist, WishlistAdmin)

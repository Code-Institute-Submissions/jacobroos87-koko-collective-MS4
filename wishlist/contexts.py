from django.shortcuts import get_object_or_404
from .models import Wishlist

# Adds the wishlist items into the session
def wishlist_items(request):
    wishlist_items = []
    if request.user.is_authenticated:
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist_items = wishlist.products.all()

    context = {
        "wishlist_items": wishlist_items,
    }

    return context

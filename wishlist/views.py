from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.contrib import messages
from .models import Wishlist
from products.models import Product


def view_wishlist(request):
    return render(request, 'wishlist/wishlist.html')

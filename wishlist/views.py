from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.contrib import messages
from .models import Wishlist
from products.models import Product


def view_wishlist(request):
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.info(request,
                         f"{product.name} has been added to your wishlist.")
        
    else:
        messages.error(request,
                       "Error, you already have this item in your wishlist!")
    return redirect(reverse("product_detail", args=product_id))

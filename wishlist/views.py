from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


@login_required
def view_wishlist(request):
    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, product_id):
    """ Adds product to wishlist """
    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.info(request,
                      f"{product.name} has been added to your wishlist.")
    else:
        messages.error(request,
                       "Error, you already have this item in your wishlist!")
    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def remove_wishlist_item(request, product_id):
    """ Removes product from wishlist """
    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    origin = request.GET.get('origin')

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.info(
            request,
            f"Success! {product.name} has been removed from your wishlist!")
    else:
        messages.error(request, "Error! Please try again")

    if origin == 'wishlist':
        return redirect(reverse("view_wishlist"))
    else:
        return redirect(reverse("product_detail", args=[product_id]))


@login_required
def clear_wishlist(request):
    """ Clears all products from wishlist """
    wishlist = get_object_or_404(Wishlist, user=request.user)
    try:
        wishlist.products.clear()
        messages.info(request,
                      "Success! Your wishlist has been cleared!")
        return redirect(reverse("view_wishlist"))
    except Exception as e:
        messages.error(request, f"Error clearing wishlist {e}")
        return redirect(reverse("products"))

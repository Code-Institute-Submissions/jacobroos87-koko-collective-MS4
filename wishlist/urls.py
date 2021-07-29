from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_wishlist, name="view_wishlist"),
    path("add/<product_id>/", views.add_to_wishlist,
         name="add_to_wishlist"),
    path("remove/<product_id>/", views.remove_wishlist_item,
         name="remove_wishlist_item"),
    path("clear/", views.clear_wishlist,
         name="clear_wishlist"),
]

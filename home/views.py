from django.shortcuts import render
from products.models import Product
from products.models import Category

# Create your views here.


def index(request):
    featured_products = Product.objects.filter(is_featured=True)

    context = {
        'featured_products': featured_products,
    }

    return render(request, 'home/index.html', context)

from django.shortcuts import render, get_object_or_404
from products.models import Product
from products.models import Category

# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)

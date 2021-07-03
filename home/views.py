from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)

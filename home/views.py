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


def bad_request(request, *args, **argv):
    return render(request, 'home/400.html')


def permission_denied(request, *args, **argv):
    return render(request, 'home/403.html')


def page_not_found(request, *args, **argv):
    return render(request, 'home/404.html')


def server_error(request, *args, **argv):
    return render(request, 'home/500.html')

from django.shortcuts import render
from products.models import Product

# Create your views here.

# Renders Home Page with products in template
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


def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')

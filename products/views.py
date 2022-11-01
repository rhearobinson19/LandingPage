from django.http import HttpResponse
from django.shortcuts import render
from .models import ProductsProducts


def index(request):
    # product = Products.objects.all()
    return render(request, "index.html")

def new(request):
    return HttpResponse("Hello")

def product_list(request):
    context = {
        'title': 'products',
        'products': ProductsProducts.objects.all(),
    }
    return render(request, 'index.html', context)






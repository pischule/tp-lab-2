from django.shortcuts import render
from django.views import generic

from .models import Product

def index(request):
    num_products = Product.objects.count()

    context = {
        'num_products': num_products
    }

    return render(request, 'index.html', context=context)

class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product

from django.shortcuts import render
from django.views import generic

from .models import Product, Order, ProductInstance


def index(request):
    context = {
        'num_products': Product.objects.count(),
        'num_orders': Order.objects.count(),
        'catalog_items': ProductInstance.objects.filter(count__gt=0).count(),
    }

    return render(request, 'index.html', context=context)


class CatalogListView(generic.ListView):
    model = ProductInstance
    template_name = "store/catalog.html"

    def get_queryset(self):
        return ProductInstance.objects.filter(count__gt=0)


class ProductInstanceDetailView(generic.DetailView):
    model = ProductInstance


class ProductDetailView(generic.DetailView):
    model = Product


class OrderListView(generic.ListView):
    model = Order


class OrderDetailView(generic.DetailView):
    model = Order

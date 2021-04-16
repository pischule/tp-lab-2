from django.contrib.auth.mixins import LoginRequiredMixin
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


class OrderBuyerListView(generic.ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = ['product', 'count']

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class SellerProductListView(generic.ListView):
    model = Product
    template_name = 'store/seller_product_list.html'

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)


class SellerCreateProductView(generic.CreateView):
    fields = ['title', 'price']
    model = Product

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super(SellerCreateProductView, self).form_valid(form)


class SellerEditProductView(generic.UpdateView):
    fields = ['title', 'price']
    model = Product


class SellerProductInstanceListView(generic.ListView):
    model = ProductInstance
    template_name = 'store/seller_productinstance_list.html'

    def get_queryset(self):
        return ProductInstance.objects.filter(product__seller=self.request.user)


class SellerProductInstanceCreateView(generic.CreateView):
    model = ProductInstance
    fields = ['product', 'count']
    template_name = 'store/seller_productinstance_form.html'


class SellerProductInstanceUpdateView(generic.UpdateView):
    model = ProductInstance
    fields = ['product', 'count']
    template_name = 'store/seller_productinstance_form.html'


class BuyerProductInstanceOrder(generic.CreateView):
    model = Order
    fields = ['count']

    def form_valid(self, form):
        product_instance = ProductInstance.objects.get(pk=self.kwargs['pk'])

        if form.instance.count > product_instance.count:
            form.instance.count = None
            return super(BuyerProductInstanceOrder, self).form_invalid(form)

        form.instance.buyer = self.request.user
        form.instance.status = Order.Status.CREATED
        form.instance.product = product_instance.product

        product_instance.count -= form.instance.count
        product_instance.save()

        return super(BuyerProductInstanceOrder, self).form_valid(form)

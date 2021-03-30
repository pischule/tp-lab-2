from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-instance/<int:pk>', views.ProductDetailView.as_view(), name='productinstance-detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/buyer', views.OrderBuyerListView.as_view(), name='orders-buyer'),
    path('order/create', views.OrderCreateView.as_view(), name='order-create'),
    path('seller/products', views.SellerProductListView.as_view(), name='seller-products'),
    path('seller/product/create', views.SellerCreateProductView.as_view(), name='seller-product-create'),
    path('seller/product/<int:pk>/update', views.SellerEditProductView.as_view(), name='seller-product-update'),
    path('seller/product-instances', views.SellerProductInstanceListView.as_view(), name='seller-productinstances'),
    path('seller/product-instance/create', views.SellerProductInstanceCreateView.as_view(), name='seller-productinstance-create'),
    path('seller/product-instance/<int:pk>/update', views.SellerProductInstanceCreateView.as_view(), name='seller-productinstance-create'),

]



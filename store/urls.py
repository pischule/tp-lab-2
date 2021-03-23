from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
]



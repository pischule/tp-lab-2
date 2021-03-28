from django.contrib import admin

from .models import Product, User, Order, ProductInstance, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(OrderItem)
admin.site.register(User)

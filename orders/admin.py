from django.contrib import admin
from .models import ShopCart, OrderProduct, Order


# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']

admin.site.register(ShopCart,ShopCartAdmin)

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','total','status']
    list_filter = ['status']
    readonly_fields = ('user','phone','first_name','last_name', 'phone','total')
    can_delete = False
    inlines = [OrderProductline]

admin.site.register(Order,OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']

admin.site.register(OrderProduct,OrderProductAdmin)
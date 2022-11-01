from django.contrib import admin
from .models import ProductsProducts, ProductsOffer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(ProductsOffer, offerAdmin)
admin.site.register(ProductsProducts, ProductAdmin)

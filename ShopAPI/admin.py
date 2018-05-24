from django.contrib import admin
from ShopAPI.models import Products, Wishlist

class ProductsAdmin(admin.ModelAdmin):

    class Meta:
        model = Products


class WishlistAdmin(admin.ModelAdmin):

    class Meta:
        model = Wishlist


admin.site.register(Products)
admin.site.register(Wishlist)
from django.db import models
from django.conf import settings

class Products(models.Model):
    stock_number = models.DecimalField(max_digits= 15, decimal_places=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product_name = models.CharField(max_length = 256)
    brand_name = models.CharField(max_length =256)
    image = models.FileField(null=True, blank=True)
    create = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        # return str(self.stock_number)
        return str(str(self.product_name) + " " + str(self.brand_name) + " " + str(self.stock_number))



class Wishlist(models.Model):
    name = models.OneToOneField(Products, on_delete=models.CASCADE, primary_key=True)
    create = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.name.stock_number)







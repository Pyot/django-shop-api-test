from rest_framework import serializers

from ShopAPI.models import Products, Wishlist

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'pk',
            'product_name',
            'brand_name',
            'stock_number',
            'image',
            'user'
        ]

class ShowWishlistSerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.CharField(source='name.product_name', max_length = 256)
    brand_name = serializers.CharField(source='name.brand_name',max_length =256)
    stock_number = serializers.DecimalField(source='name.stock_number' , max_digits= 15, decimal_places=0)
    image = serializers.FileField(source='name.image')
    
    class Meta:
        model = Products
        fields = [
            'pk',
            'product_name',
            'brand_name',
            'stock_number',
            'image'
        ]

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wishlist
        fields = [
            'name'
        ]
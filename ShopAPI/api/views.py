import json

from rest_framework.generics import ListAPIView
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder


from ShopAPI.models import Products, Wishlist
from .serializers import ProductsSerializer, WishlistSerializer, ShowWishlistSerializer


class ProductsAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = ProductsSerializer
    passed_id                   = None
    queryset                    = Products.objects.all()

    # def get_queryset(self):
    #     request = self.request
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductsDetailsAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsSerializer
    lookup_field                = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class WishlistAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = WishlistSerializer
    passed_id                   = None
    queryset                    = Wishlist.objects.all()
  

    # def get_queryset(self):
    #     request = self.request
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
      
    #     qs =Wishlist.objects.all()
    #     nexte = qs

    #     # qs =Wishlist.objects.all().values('name__brand_name')
    #     # nexte = json.dumps(list(qs), cls=DjangoJSONEncoder)
    #     return nexte


class WishlistDetailsAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Wishlist.objects.all()
    serializer_class            = WishlistSerializer
    lookup_field                = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class ShowWishlistAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = ShowWishlistSerializer
    passed_id                   = None
    queryset                    = Wishlist.objects.all()

    # def get_queryset(self):
    #     request = self.request
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)






    


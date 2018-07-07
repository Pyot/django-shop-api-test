from django.contrib import admin
from django.conf.urls import url



from .views import (
    ProductsAPIView,
    ProductsDetailsAPIView,
    WishlistAPIView,
    WishlistDetailsAPIView,
    ShowWishlistAPIView,
    ShowOnly
)

urlpatterns = [
    url(r'^products/$', ProductsAPIView.as_view()),
    url(r'^products/(?P<pk>\d+)/$', ProductsDetailsAPIView.as_view()),
    url(r'^wishlist/$', WishlistAPIView.as_view()),
    url(r'^wishlist/(?P<pk>\d+)/$', WishlistDetailsAPIView.as_view()),
    url(r'^showwishlist/$', ShowWishlistAPIView.as_view()),
    url(r'^showonly/$', ShowOnly.as_view()),

    
]
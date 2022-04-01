# from main.api.views import ContactAPIView, MainPageMarkaAPIView, WishlistAPIView , MainPageModelAPIView, FilteredProductAPIView
from collections import namedtuple
from product.views import AddProductPageView
from django.urls import path
from product.api.views import *



app_name = 'productapi'
urlpatterns = [
    path('add-product/',CreatePoruct.as_view(),name='create-product'),
    path('city/',CityAPIView.as_view(),name='city'),
    path('category/',CategoryApiView.as_view(),name='category-api'),
    path('product-detail/<str:slug>', ProductDetail.as_view(), name='product-detail'),
    path("add-product-marka/" , AddProductMarkaAPIView.as_view(), name='add-product-marka'),
    path("add-product-model/" , AddProductModelAPIView.as_view(), name='add-product-model')
    # path('category-detail/',CategoryDetail.as_view(),name='category-detail-api'),
]
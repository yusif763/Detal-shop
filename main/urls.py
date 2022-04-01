from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('allbrands/',AllBrandsView.as_view(),name='allbrands'),
    path('brands/<str:slug>/',BrandsView.as_view(),name='brands'),
    path('car-filter/',CarFilterView.as_view(),name='car-filter'),
    path('car-detail/<str:model_slug>/<str:marka_slug>/',CarDetailView.as_view(),name='car-detail'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('shops/',ShopsView.as_view(),name='shops'),
    path('shops/<str:slug>/',ShopDetailView.as_view(),name='shop_detail'),
    path('inner-details/<str:model_slug>/<str:marka_slug>/<str:parent_detail_slug>/<str:subparent_detail_slug>/',InnerDetailView.as_view(),name='inner-details'),
    path('single-page/',SinglePageView.as_view(),name='isingle-page'),
    path('searched-products/',SearchedProdsView.as_view(),name='searched'),
    
    path('sub-parts/<str:model_slug>/<str:marka_slug>/<str:parent_detail_slug>/',SubParts.as_view(),name='sub-parts'),

    path('wishlist/<str:slug>',WishlistPageView.as_view(),name='wishlist'),
    path('set_language/', change_language, name="set_language")
]
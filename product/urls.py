from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('',ProductPageView.as_view(),name='products'),
    path('add-product/',AddProductPageView.as_view(),name='add-product'),
    path('single-product/<str:slug>/',SingleProductView.as_view(),name='single-product'),
    path('sale-products/',SaleProductPageView.as_view(),name='sale-products'),
    path('update-product/<str:slug>/',UpdateProduct.as_view(),name='update-product'),
    path('<str:model_slug>/<str:marka_slug>/<str:parent_detail_slug>/<str:subparent_detail_slug>/<str:child_detail_slug>/',FilteredProducts.as_view(),name='filtered-products'),
]
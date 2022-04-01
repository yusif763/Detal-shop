from main.api.views import ActivateProductAPIView, ContactAPIView, MainPageMarkaAPIView, UserRatingAPIView, WishlistAPIView, MainPageModelAPIView, FilteredProductAPIView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'mainapi'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('wishlist/', WishlistAPIView.as_view(), name='wishlist'),
    path('main/', MainPageMarkaAPIView.as_view(), name='main'),
    path('main-model/', MainPageModelAPIView.as_view(), name='main-model'),
    path('filtered-prod/', FilteredProductAPIView.as_view(), name='filtered-prod'),
    path('activate-product', ActivateProductAPIView.as_view(), name='activate-product'),
    path('user-rating/<slug:slug>', UserRatingAPIView.as_view(), name='user-rating'),
]

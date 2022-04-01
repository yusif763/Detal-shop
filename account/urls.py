from django.urls import path,re_path
from account.views import *
from django.contrib.auth.views import LogoutView
app_name = 'account'

urlpatterns = [
    path('login/',LoginPageView.as_view(),name='login'),
    path('register/',RegisterPageView.as_view(),name='register'),
    path('self-profile/<str:slug>/',SelfProfilePageView.as_view(),name='self-profile'),
    path('user-profile/<str:slug>/',UserProfilePageView.as_view(),name='user-profile'),
    path('user-profile2/<str:slug>/',UserProfile2PageView.as_view(),name='user-profile2'),
    path('change-password/',ChangePasswordPageView.as_view(),name='change-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forget-password/',ForgetPasswordView.as_view(),name='forget-password'),
    # re_path(r'password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/<uidb64>/<token>/', 
         CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
]
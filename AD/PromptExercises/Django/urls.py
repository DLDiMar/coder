from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('bad_redirect/', views.bad_redirect, name='bad_redirect'),
]
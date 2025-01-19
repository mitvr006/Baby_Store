# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('seller-header/', views.seller_header, name='seller_header'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller-product/', views.seller_product, name='seller_product'),
    path('seller-login/', views.seller_login, name='seller_login'),
    path('seller-register/', views.seller_register, name='seller_register'),
    path('logout/', views.logout_view, name='logout'),
]

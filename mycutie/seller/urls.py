# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('seller-page/', views.seller_page, name='seller_page'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('seller-login/', views.seller_login, name='seller_login'),
    path('seller-register/', views.seller_register, name='seller_register'),
    path('logout/', views.logout_view, name='logout'),
]

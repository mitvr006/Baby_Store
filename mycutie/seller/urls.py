# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('seller-header/', views.seller_header, name='seller_header'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller-product/', views.seller_product, name='seller_product'),
    path('seller-login/', views.seller_login, name='seller_login'),
    path('seller-register/', views.seller_register, name='seller_register'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

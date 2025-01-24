# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('seller-home/', views.seller_home, name='seller_home'),
    path('seller-header/', views.seller_header, name='seller_header'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),

    path('view-products/', views.view_products, name='view_products'),
    path('view-orders/', views.view_orders, name='view_orders'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('remove-product/<int:product_id>/', views.remove_product, name='remove_product'),

    path('seller-login/', views.seller_login, name='seller_login'),
    path('seller-register/', views.seller_register, name='seller_register'),
    path('logout/', views.logout_view, name='logout'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import signup, login_view, logout_view, add_product, product_list, product_detail, buy_product, search_products, category_products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),  
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'), 
    path('add/product/', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path('search/', search_products, name='search_products'),
     path('category/<int:category_id>/', category_products, name='category_products'),

]


if settings.DEBUG:  # Serve media only during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



     


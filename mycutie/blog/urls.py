from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import signup, login_view, logout_view, add_product, product_list

urlpatterns = [
    path('signup/', signup, name='signup'),  
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'), 
    path('add/product/', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),

]




     


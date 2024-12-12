from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import signup, login_view, logout_view, product_list, cart_detail, add_to_cart, remove_from_cart, update_cart

urlpatterns = [
    path('signup/', signup, name='signup'),  
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'), 
    path('products/', product_list, name='product_list'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', update_cart, name='update_cart'),

]



     


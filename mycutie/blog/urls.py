from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import signup, login_view, logout_view, product_list, cart_detail, add_to_cart, remove_from_cart

urlpatterns = [
    path('signup/', signup, name='signup'),  
    path('login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'), 

]



     


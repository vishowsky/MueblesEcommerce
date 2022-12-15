from django.urls import path
from . import views
from  tienda.controller import authview, cart

urlpatterns = [
    path('', views.home, name="home"),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<str:slug>', views.catalogview, name="catalogview"),
    path('catalog/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/', authview.register, name="register"),
    path('login/',authview.loginpage, name='loginpage'),
    path ('logout/',authview.logoutpage, name="logout"),

   path('add-to-cart', cart.addtocart, name="addtocart" ),
   path('cart', cart.viewcart, name="cart"),
   path('update-cart', cart.updatecart, name="updatecart"),
   path('delete-cart-item', cart.deletecartitem, name="deletecartitem")
]
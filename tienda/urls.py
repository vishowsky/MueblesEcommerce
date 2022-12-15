from django.urls import path
from . import views
from  tienda.controller import authview

urlpatterns = [
    path('', views.home, name="home"),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<str:slug>', views.catalogview, name="catalogview"),
    path('catalog/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/', authview.register, name="register"),
    path('login/',authview.loginpage, name='loginpage'),
    path ('logout/',authview.logoutpage, name="logout")

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<str:slug>', views.catalogview, name="catalogview"),
    path('catalog/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview")
]
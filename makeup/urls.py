from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands', views.brandList, name='brands'),
    path('products', views.productList, name='products'),
    path('brand/<int:id>', views.brandDetail, name='brand'),
    path('product/<int:id>', views.productDetail, name='product'),
    
]
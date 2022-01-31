from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('brands', views.brandList, name='brands'),
    path('products', views.productList, name='products'),
    path('brand/<int:id>', views.brandDetail, name='brand'),
    path('product/<int:id>', views.productDetail, name='product'),
    path('brand-create/', views.brandCreate, name='brand-create'),
    path('brand-update/<int:id>', views.brandCreate, name='brand-update'),
    path('brand-delete/<int:id>', views.brandDelete, name='brand-delete'),
  #  path('brandSave/', views.brandSave, name='brandSave'),
    
]
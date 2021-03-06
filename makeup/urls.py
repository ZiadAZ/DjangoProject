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
    path('product-manage/', views.productManage, name='product-manage'),
    path('product-update/<int:id>', views.productManage, name='product-update'),
    path('product-delete/<int:id>', views.productDelete, name='product-delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
  #  path('brandSave/', views.brandSave, name='brandSave'),
    
]
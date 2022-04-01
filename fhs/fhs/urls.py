"""fhs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import *
from pages import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.food, name='home'),
    path('register/', views.register, name='register'),
    path('search/', views.search_food, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login1.html'), name='login'),
    path('search/login/', auth_views.LoginView.as_view(template_name='pages/login1.html')),
    path('cart/login/', auth_views.LoginView.as_view(template_name='pages/login1.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name=' '), name='logout'),
    path('profile/',views.profile,name='profile'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:food_id>', views.add_cart, name='add_item'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'), 
    path('diet/',views.diet,name='diet'),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
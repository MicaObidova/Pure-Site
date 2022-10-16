from django.contrib import admin
from django.urls import path, include
from main.views import *
urlpatterns = [
    path('', index, name='index'),
    path('blog-single/<int:pk>/', blogview, name='blog-single'),
    path('about', about, name='about'),
    path('blog',blog,name='blog'),
    path('cart', cart,name='cart'),
    path('checkout',checkout,name='checkout'),
    path('contact', contact,name='contact'),
    path('product-single/<int:pk>/', productviews, name='product-single'),
    path('profile', profile,name='profile'),
    path('service', service,name='service'),
    path('shop', shop, name='shop'),
    path('search/', Search, name='search'),
    path('searching/', Searching, name='searching'),
    path('login/', ForLogin, name='login'),
    path('registration/', Registration, name='registration'),
    path('logout/', LogOutView, name='logout'),
    path('add-card/<int:pk>/', AddCard, name='add-card'),
    path('delete-card/<int:pk>/', DeleteCard, name='delete-card'),
    path('checkout/', CheckoutView, name='checkout'),
    path('order/', OrderView, name='order'),
    path('add-comment/',ADDcomment,name='add-comment'),
    path('searchblog/', SearchBlog, name='searchblog'),
]
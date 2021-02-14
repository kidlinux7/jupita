from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home,name='home'),
    path('products_details/<int:pk>/',views.products_details,name='products_details'),
    path('blog',views.blog,name='blog'),
    path('blog_details/<int:pk>/',views.blog_details,name='blog_details'),
]
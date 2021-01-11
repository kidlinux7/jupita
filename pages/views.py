from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    product = Products.objects.all()
    news = Blog.objects.all()
    context = {'product':product,'news':news}
    return render(request,"index.html",context)

def products_details(request, **kwargs):
    pk = kwargs.get('pk')
    products = Products.objects.get(id=pk)
    context = {'products':products}
    return render(request,'product.html',context)

def blog(request):
    news = Blog.objects.all()
    context = {'news':news}
    return render(request,"blog.html",context)

def blog_details(request, **kwargs):
    pk = kwargs.get('pk')
    individual_news = Blog.objects.get(id=pk)
    context = {'individual_news':individual_news}
    return render(request,"individual_blog.html",context)
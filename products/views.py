from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category,Product
# Create your views here.



def ogrenci(request):
    category = Category.objects.filter(id=1)
    products=Product.objects.filter(category__parent_id=1)
    context = {'category': category, 'products' : products }
    return render(request,'product/ogrenci.html',context)


def kirtasiye(request):
    product=Product.objects.filter(category_id=4)
    return render(request,'product/kirtasiye.html',{'product':product})

def elektronik(request):
    product=Product.objects.filter(category_id=5)
    return render(request, 'product/elektronik.html', {'product': product})

def cocukgiyim(request):
    product = Product.objects.filter(category_id=9)
    return render(request, 'product/cgiyim.html', {'product': product})


def yardim(request):
    category = Category.objects.filter(id=2)
    products = Product.objects.filter(category__parent_id=2)
    context = {'category': category, 'products': products}
    return render(request, 'product/gidagiyimevesyasi.html', context)


def giyim(request):
    product = Product.objects.filter(category_id=7)
    return render(request, 'product/giyim.html', {'product': product})


def gida(request):
    product = Product.objects.filter(category_id=8)
    return render(request, 'product/gida.html', {'product': product})


def esya(request):
    product = Product.objects.filter(category_id=6)
    return render(request, 'product/evesyasi.html', {'product': product})
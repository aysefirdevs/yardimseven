from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect

# Create your views here.
from .models import ShopCart, ShopCartForm
from products.models import Category


@login_required(login_url='/accounts/login/')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    #------ürün sepette var mı kontrolü----
    checkproduct=ShopCart.objects.filter(product_id=id) #ürün sepette var mı sorgusu
    if checkproduct:
        control = 1  #ürün sepette var
    else:
        control = 0  #ürün sepette yokk

    if request.method == 'POST':   #form post edildiyse
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:  #ürün varsa güncelle
                data=ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else: #ürün yoksa ekle
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()

        messages.success(request, "Ürün başarı ile eklenmiştir. Teşekkür ederiz.")
        return HttpResponseRedirect(url)

    messages.warning(request, "ürünü sepete eklemede bir hata oluştu..")
    return HttpResponseRedirect(url)



@login_required(login_url='/accounts/login/')
def shopcart(request):
    category=Category.objects.all()
    current_user=request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0

    for rs in schopcart:
        total += rs.product.price * rs.quantity

    context={
        'schopcart': schopcart,
        'category' : category,
        'total' : total
    }
    return render(request,'orders/shopcart_products.html',context)

@login_required(login_url='/accounts/login/')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"ürün sepetten silindi.")
    return HttpResponseRedirect('/shopcart')
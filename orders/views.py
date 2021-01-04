from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect

# Create your views here.
from .models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct
from products.models import Category,Product
from accounts.models import User



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


    total=0
    for rs in schopcart:
        total += rs.product.price * rs.quantity
        total=round(total,2)

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

@login_required(login_url='/accounts/login/')
def orderproduct(request):
    category=Category.objects.all()
    current_user=request.user
    schopcart=ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity
        total = round(total, 2)

    if request.method == 'POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            data=Order()
            data.first_name=form.cleaned_data['first_name']
            data.last_name=form.cleaned_data['last_name']
            data.phone=form.cleaned_data['phone']
            data.user_id=current_user.id
            data.total=total
            data.save()

            schopcart=ShopCart.objects.filter(user_id=current_user.id)
            for rs in schopcart:
                detail=OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product.id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

                product= Product.objects.get(id=rs.product_id)
                product.amount -=rs.quantity
                product.save()


            ShopCart.objects.filter(user_id=current_user.id).delete()
            messages.success(request,'siparişiniz alındı. Teşekkürler')
            return render(request, 'orders/order_completed.html',{'category':category})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/orders/orderproduct')

    form=OrderForm()
    context={
        'schopcart': schopcart,
        'category': category,
        'form' : form,
        'total':total,
    }
    return render(request,'orders/Order_Form.html',context)

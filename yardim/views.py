from msilib.schema import ListView

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import IhtiyacForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import Ihtiyac, Carousel,Bagis,BagisForm,BagisPayment,BagisPaymentForm

STATUS = "published"

class IndexView(ListView):

    template_name= 'yardim/index.html'
    model=Ihtiyac
    context_object_name = 'ihtiyaclar'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(IndexView, self).get_context_data(**kwargs)
        context['images'] = Carousel.objects.filter(
            status="published",
        ).exclude(cover_image='')
        return context


#def carousel(request):
 #   context = dict()
 #   context['images'] = Carousel.objects.filter(
  #      status="published",
 #   ).exclude(cover_image='')
 #   return render(request, 'yardim/index.html', context)"""


class detay(DetailView):
    template_name = 'yardim/detay.html'
    model=Ihtiyac
    context_object_name = 'ihtiyaclar'


    def get_context_data(self, **kwargs):
        context = super(detay, self).get_context_data(**kwargs)
        context['previous']=Ihtiyac.objects.filter(id__lt=self.kwargs['pk']).order_by('-pk').first()
        context['next']=Ihtiyac.objects.filter(id__gt=self.kwargs['pk']).order_by('pk').first()
        return context



def hakkimizda(request):
    return render(request,'yardim/hakkimizda.html')

def bizeulasin(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request,'yardim/bizeulasin.html',
                  { 'mapbox_access_token': mapbox_access_token })


def ihtiyacekle(request):
    form=IhtiyacForm(request.POST or None)
    if form.is_valid():
        ihtiyac=form.save(commit=False)
        ihtiyac.user= request.user
        ihtiyac.save()

        messages.success(request,"İhtiyaç başarıyla oluşturuldu.")
        return redirect('ihtiyaclarim')

    return render(request,'yardim/ihtiyacekle.html',{'form':form})

def ihtiyaclarim(request):
    ihtiyaclar=Ihtiyac.objects.filter(user=request.user)

    context={
        'ihtiyaclar': ihtiyaclar
    }

    return render(request, 'yardim/ihtiyaclarim.html',context)


def detail(request,id):
    ihtiyaclar=Ihtiyac.objects.filter(id=id).first()
    return render(request,'yardim/detail.html',{'ihtiyaclar':ihtiyaclar})


def updateIhtiyac(request,id):
    ihtiyac=get_object_or_404(Ihtiyac,id=id)
    form=IhtiyacForm(request.POST or None,request.FILES or None,instance=ihtiyac)
    if form.is_valid():
        ihtiyac = form.save(commit=False)
        ihtiyac.user = request.user
        ihtiyac.save()

        messages.success(request, "İhtiyaç başarıyla güncellendi.")
        return redirect('ihtiyaclarim')


    return render(request,'yardim/update.html',{'form':form})


def deleteIhtiyac(request,id):
    ihtiyac = get_object_or_404(Ihtiyac, id=id)
    ihtiyac.delete()
    messages.success(request,"İhtiyaç silindi.")

    return redirect('ihtiyaclarim')


def koyokullari(request):
    ihtiyaclar = Ihtiyac.objects.all()
    return render(request, 'yardim/koyokullari.html', {'ihtiyaclar': ihtiyaclar})


@login_required(login_url='/accounts/login/')
def odemebagis(request,id):
    current_user = request.user
    iht=Ihtiyac.objects.get(id=id)
    if request.method == 'POST':
        form=BagisForm(request.POST)
        if form.is_valid():
            data=Bagis()
            data.user_id=current_user.id
            data.ihtiyac_id=iht.id
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.tutar=iht.sum
            data.save()

            Ihtiyac.objects.filter(id=id).delete()
            messages.success(request, 'bağışınız alındı. Teşekkürler')
            return render(request, 'yardim/bagiscompleted.html', {'iht': iht})

        else:
            messages.warning(request, form.errors)

    form = BagisForm()
    context = {
        'iht': iht,
        'form': form,
        'tutar':iht.sum,
    }
    return render(request,'yardim/odeme.html',context)


def payment(request,id):
    current_user = request.user
    tip = id
    if request.method == 'POST':
        form = BagisPaymentForm(request.POST)
        if form.is_valid():
            data = BagisPayment()
            data.user_id = current_user.id
            data.tutar = form.cleaned_data['tutar']
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.tip = id
            data.save()

            messages.success(request, 'bağışınız alındı. Teşekkürler')
            return render(request, 'yardim/bagiscompleted.html')

        else:
            messages.warning(request, form.errors)


    form=BagisPaymentForm()
    context={'tip':tip, 'form':form}

    return render(request,'yardim/payment.html',context)

from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.template.context_processors import request
from django.views.generic import CreateView
from .forms import RegisterForm,ORegisterForm,LoginForm,OLoginForm
from .models import User
from django.contrib import messages

# Create your views here.


def Login(request):
    form=LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı.")
            return render(request, 'accounts/login.html', context)


        messages.success(request, "Başarıyla giriş yaptınız.")
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/login.html', context)



class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']='bagisci'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('index')


def logoutUser(request):
    logout(request)
    return redirect('index')



class ORegisterView(CreateView):
    model = User
    form_class = ORegisterForm
    template_name = 'accounts/oregister.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ogretmen'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



def OLogin(request):
    form=OLoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı.")
            return render(request, 'accounts/ologin.html', context)


        messages.success(request, "Başarıyla giriş yaptınız.")
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/ologin.html', context)



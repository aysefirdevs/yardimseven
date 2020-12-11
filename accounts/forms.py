from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Bagisci,User,Ogretmen

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model=User

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_bagisci=True
        user.save()
        bagisci=Bagisci.objects.create(user=user)
        bagisci.username=self.cleaned_data.get('username')
        bagisci.save()

        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı adı')
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)

class ORegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username=forms.CharField(required=True)
    telefon = forms.CharField(required=True)
    kimlik = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_ogretmen = True
        user.save()
        ogretmen = Ogretmen.objects.create(user=user)
        ogretmen.username = self.cleaned_data.get('username')
        ogretmen.telefon = self.cleaned_data.get('telefon')
        ogretmen.kimlik = self.cleaned_data.get('kimlik')
        ogretmen.save()

        return user

class OLoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı adı')
    password = forms.CharField(label='Parola', widget=forms.PasswordInput)


from django import forms
from .models import Ihtiyac,Contact


class IhtiyacForm(forms.ModelForm):
    class Meta:
        model=Ihtiyac
        fields = ['title', 'city', 'content','sum']
        widgets= {
            'title':forms.TextInput(attrs={'placeholder': 'Başlık giriniz.'}),
            'city':forms.TextInput(attrs={'placeholder':'Şehir ekleyiniz'}),
            'content':forms.Textarea(attrs={'placeholder':'İhtiyaç ayrıntılarınızı belirtiniz.(Okulunuzun adı, ihtiyacı vb.)'}),
            'sum':forms.NumberInput(attrs={'placeholder':'İhtiyaç maliyetini TL cinsinden belirtiniz.'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','konu','mesaj']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad Soyad'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'konu': forms.TextInput(attrs={'placeholder': 'Konu'}),
            'mesaj': forms.Textarea(
                attrs={'placeholder': 'Mesajınız..'}),

        }


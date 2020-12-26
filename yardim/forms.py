from django import forms
from .models import Ihtiyac


class IhtiyacForm(forms.ModelForm):
    class Meta:
        model=Ihtiyac
        fields = ['title', 'city', 'content','sum']
        widgets= {
            'title':forms.TextInput(attrs={'placeholder': 'Başlık giriniz'}),
            'city':forms.TextInput(attrs={'placeholder':'Şehir ekleyiniz'}),
            'content':forms.Textarea(attrs={'placeholder':'İhtiyaç ayrıntılarınızı belirtiniz.'}),
            'sum':forms.NumberInput(attrs={'placeholder':'İhtiyaç maliyetini TL cinsinden belirtiniz.'})
        }


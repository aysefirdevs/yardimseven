from django.conf import settings
from django.db import models
from django.forms import ModelForm
from accounts.models import User

DEFAULT_STATUS="draft"

STATUS={
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
}


class Ihtiyac(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Ogretmen')
    title=models.CharField(max_length=100,verbose_name='Başlık')
    content=models.TextField(verbose_name='İhtiyaç İçeriği')
    sum=models.FloatField(verbose_name='Maliyet')
    city=models.CharField(max_length=50,verbose_name='Şehir')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    title=models.CharField(max_length=200, blank=True, null=True)
    cover_image=models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now=True)
    uptated_at=models.DateTimeField(auto_now=True)



class Bagis(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ihtiyac=models.ForeignKey(Ihtiyac,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    tutar=models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class BagisForm(ModelForm):
    class Meta:
        model=Bagis
        fields=['first_name','last_name','phone']


class BagisPayment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    tutar = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    tip=models.IntegerField()

    def __str__(self):
        return self.user.first_name


class  BagisPaymentForm(ModelForm):
    class Meta:
        model=BagisPayment
        fields=['tutar','first_name','last_name','phone']



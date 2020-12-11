from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_bagisci = models.BooleanField(default=False)
    is_ogretmen = models.BooleanField(default=False)


class Bagisci(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username


class Ogretmen(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    telefon=models.CharField(max_length=50)
    kimlik=models.CharField(max_length=11)


    def __str__(self):
        return self.user.username
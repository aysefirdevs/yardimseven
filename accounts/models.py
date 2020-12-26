from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_bagisci=models.BooleanField(default=False)
    is_ogretmen=models.BooleanField(default=False)
    telefon=models.CharField(max_length=50)
    kimlik=models.CharField(max_length=11)
from django.urls import path, include
from . import views

urlpatterns = [
    path('veriokuma/',views.veriokuma, name="veriokuma"),

]
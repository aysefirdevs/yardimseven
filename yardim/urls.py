from django.conf.urls import url
from django.urls import path
from .views import *
from . import views


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('hakkimizda/',views.hakkimizda, name='hakkimizda'),
    path('bizeulasin/',views.bizeulasin, name='bizeulasin'),

]

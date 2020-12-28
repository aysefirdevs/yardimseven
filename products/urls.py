from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

#from .views import category

urlpatterns = [

    path('ogrenci/',views.ogrenci, name='ogrenci'),
    path('ogrenci/kirtasiye',views.kirtasiye,name='kirtasiye'),
    path('ogrenci/elektronik',views.elektronik, name='elektronik'),
    path('ogrenci/cgiyim',views.cocukgiyim, name='cgiyim'),
    path('yardim/',views.yardim, name='yardim'),
    path('yardim/giyim',views.giyim, name='giyim'),
    path('yardim/gida',views.gida, name='gida'),
    path('yardim/esya',views.esya, name='esya'),
 #   path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),

]
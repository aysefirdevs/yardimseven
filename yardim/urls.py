from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('hakkimizda/',views.hakkimizda, name='hakkimizda'),
    path('bizeulasin/',views.bizeulasin, name='bizeulasin'),
    path('ihtiyacekle/',views.ihtiyacekle,name='ihtiyacekle'),
    path('ihtiyaclarim/',views.ihtiyaclarim,name='ihtiyaclarim'),
    path('ihtiyaclarim/ihtiyac/<int:id>',views.detail,name='detail'),
    path('ihtiyaclarim/update/<int:id>',views.updateIhtiyac,name='update'),
    path('ihtiyaclarim/delete/<int:id>',views.deleteIhtiyac,name='delete'),
    path('detay/<int:pk>',detay.as_view(), name='detay'),
    path('koyokullari/',views.koyokullari,name='koyokullari'),


]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

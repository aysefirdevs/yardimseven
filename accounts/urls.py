from django.urls import path
from . import views
from .views import RegisterView,Login,ORegisterView,OLogin



urlpatterns = [
    path('login/',Login,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('register/', RegisterView.as_view(), name='bagisci_signup'),
    path('oregister/',ORegisterView.as_view(), name='ogretmen_signup'),
    path('ologin/',OLogin,name='ologin'),
    path('order/',views.order, name='order'),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),
    path('bagislarim/',views.koybagislarim, name='koybagislarim'),



]
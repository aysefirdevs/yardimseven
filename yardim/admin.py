from django.contrib import admin
from .models import Ihtiyac,Carousel,BagisPayment,Contact,Arsiv,Bagis
# Register your models here.

@admin.register(Ihtiyac)
class IhtiyacAdmin(admin.ModelAdmin):
    list_display = ['title','user','content','sum','city','created_date']

    list_display_links = ['title','city','sum']
    search_fields = ['sehir','created_date','sum']
    class Meta:
        model=Ihtiyac

class ArsivAdmin(admin.ModelAdmin):
    list_display = ['user','isim','sehir','content','tutar','create_at']
    list_display_links = ['user','isim']
    class Meta:
        model=Arsiv

admin.site.register(Arsiv,ArsivAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'cover_image',
        'status',
        'created_at',

    ]
    list_filter = ['status', ]
    list_editable = list_filter

admin.site.register(Carousel, CarouselAdmin)

class BagisPaymentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        "first_name",
        "last_name",
        'phone',
        'tutar',
        'tip',
    ]
    list_filter = ['tip', ]

admin.site.register(BagisPayment,BagisPaymentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','konu','mesaj']

admin.site.register(Contact,ContactAdmin)

class BagisAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'phone',
        'tutar',
        'create_at',
    ]
    list_display_links = ['user']

admin.site.register(Bagis,BagisAdmin)
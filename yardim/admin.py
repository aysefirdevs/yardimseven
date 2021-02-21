from django.contrib import admin
from .models import Ihtiyac,Carousel,BagisPayment,Contact
# Register your models here.

@admin.register(Ihtiyac)
class IhtiyacAdmin(admin.ModelAdmin):
    list_display = ['title','user','sum','city','created_date']

    list_display_links = ['title','city','sum']
    search_fields = ['sehir','created_date','sum']
    class Meta:
        model=Ihtiyac



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
from django.contrib import admin
from .models import Ihtiyac,Carousel
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
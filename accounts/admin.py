from django.contrib import admin
from .models import User,Ogretmen,Bagisci
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_bagisci','is_ogretmen')

admin.site.register(User,UserAdmin)



admin.site.register(Bagisci)

class OgrAdmin(admin.ModelAdmin):
    list_display = ('kimlik','username','telefon')

admin.site.register(Ogretmen,OgrAdmin)


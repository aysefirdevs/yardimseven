from msilib.schema import ListView

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name= 'yardim/index.html'


def hakkimizda(request):
    return render(request,'yardim/hakkimizda.html')

def bizeulasin(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request,'yardim/bizeulasin.html',
                  { 'mapbox_access_token': mapbox_access_token })
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section


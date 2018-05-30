import json
import requests  
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
#Import Personales
from .models import Tramite, Guia

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def mostrar_guia(request, id_guia):
    guia = Guia.objects.get(pk=id_guia)
    return render(request, 'mostrar_guia.html', {'guia': guia})


def getws_organismos(request):
    r = requests.get('http://organigrama.jujuy.gob.ar/webserv_org')
    organismos = r.text
    return HttpResponse(organismos) 

def ws_tramites(request):
    tramites = [tr.as_dict() for tr in Tramite.objects.filter(activo=True)]
    
    return HttpResponse(json.dumps({"data": tramites}), content_type='application/json')

def ws_guias(request):
    guias = [guia.as_dict() for guia in Guia.objects.filter(activo=True)]    
    return HttpResponse(json.dumps({"data": guias}), content_type='application/json')

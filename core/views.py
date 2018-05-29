import json
import requests  
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
#Import Personales
from .models import Tramite

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def getws_organismos(request):
    r = requests.get('http://organigrama.jujuy.gob.ar/webserv_org')
    organismos = r.text
    return HttpResponse(organismos) 

def ws_tramites(request):
    tramites = [tr.as_dict() for tr in Tramite.objects.filter(activo=True)]
    return HttpResponse(json.dumps({"data": tramites}), content_type='application/json')
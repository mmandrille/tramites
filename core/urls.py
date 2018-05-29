from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.home, name='home'),
    #url('test', views.getws_organismos, name='getws_organismos'),

    url('ws_tramites', views.ws_tramites, name="ws_tramites"),
]
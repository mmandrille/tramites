from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.home, name='home'),
    path('guia/<int:id_guia>/', views.mostrar_guia, name='mostrar_guia'),

    #Consumir un WebService Ajeno:
#   url('test', views.getws_organismos, name='getws_organismos'),
    #Web Services JSON:
    url('ws_tramites', views.ws_tramites, name="ws_tramites"),
]
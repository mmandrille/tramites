from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.home, name='home'),
    path('guia/<int:id_guia>/', views.mostrar_guia, name='mostrar_guia'),

    #Web Services JSON:
    url('ws_tramites', views.ws_tramites, name="ws_tramites"),
]
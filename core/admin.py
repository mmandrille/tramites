from django.contrib import admin

from .models import Tramite, Guia, Archivo

#Definimos Inline
class TramiteAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'organismo']

class ArchivoInline(admin.TabularInline):
    model = Archivo

class GuiaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'organismo']
    inlines = [
        ArchivoInline,
    ]

# Register your models here.
admin.site.register(Tramite, TramiteAdmin)
admin.site.register(Guia, GuiaAdmin)
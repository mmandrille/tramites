from django.contrib import admin

from .models import Tramite, Guia, Archivo

#Definimos Inline
#Definimos inline
class ArchivoInline(admin.TabularInline):
    model = Archivo

class GuiaAdmin(admin.ModelAdmin):
    inlines = [
        ArchivoInline,
    ]

# Register your models here.
admin.site.register(Tramite)
admin.site.register(Guia, GuiaAdmin)

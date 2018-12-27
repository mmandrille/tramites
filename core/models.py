#Importamos modulos standars
import json
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from tinymce.models import HTMLField
import requests  
#Import personales
from tramites.settings import MEDIA_URL

#Choice Field
def obtener_organismos():#Funcion que obtiene del sistema de organigrama los organismos disponibles
	r = requests.get('http://organigrama.jujuy.gob.ar/ws_org/')
	orgs = json.loads(r.text)['data']
	organismos = list()
	for org in orgs:
		organismos.append((org['id'],org['nombre']))
	return organismos

# Create your models here.
class Tramite(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	organismo = models.PositiveIntegerField(choices= obtener_organismos(), default=0)
	descripcion = models.CharField(max_length=200)
	link = models.URLField()
	icono = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
	activo = models.BooleanField(default=True)
	online = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre
	def as_dict(self):
#		if self.icono is None:
#			self.icono = ''
		return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
			"link": self.link,
#			"icono": self.icono.url,
        }

#String Default para la descripcion
texto_default= '<p><strong>Detalle del Tramite</strong></p>\r\n<ul>\r\n<li>Destinatarios:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Finalidad del tr&aacute;mite:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>&Aacute;rea / Dependencia:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Referente / Responsable:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Domicilio/s donde se realiza:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>D&iacute;as y Horarios:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Requisitos a cumplimentar:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Formularios y Documentaci&oacute;n requerida:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Procedimiento:</li>\r\n</ul>\r\n<p style="padding-left: 60px;">&nbsp;</p>\r\n<ul>\r\n<li>Contacto</li>\r\n<ul>\r\n<li>Telefono:</li>\r\n<li>Email:</li>\r\n</ul>\r\n</ul>'

class Guia(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	organismo = models.PositiveIntegerField(choices= obtener_organismos(), default=0)
	descripcion = HTMLField(default=texto_default)
	icono = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), blank=True, null=True)
	activo = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre
	def as_dict(self):
#		if self.icono is None:
#			self.icono = ''
		return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
			"link": 'http://tramites.jujuy.gob.ar/guia/' + str(self.id),
#			"icono": self.icono.url,
        }

class Archivo(models.Model):
	guia = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name='archivos')
	nombre = models.CharField(max_length=50, unique=True)
	archivo = models.FileField(upload_to='')
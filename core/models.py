#Importamos modulos standars
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from tinymce.models import HTMLField

#Import personales
from tramites.settings import MEDIA_URL

# Create your models here.
class Tramite(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
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

class Guia(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = HTMLField()
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
			"link": '/guia/' + str(self.id),
#			"icono": self.icono.url,
        }

class Archivo(models.Model):
	guia = models.ForeignKey(Guia, on_delete=models.CASCADE, related_name='archivos')
	nombre = models.CharField(max_length=50, unique=True)
	archivo = models.FileField(upload_to='')
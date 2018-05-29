#Importamos modulos standars
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
#from tinymce.models import HTMLField

#Import personales
from tramites.settings import MEDIA_URL

# Create your models here.
class Tramite(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=200)
	link = models.URLField()
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
			"link": self.link,
#			"icono": self.icono.url,
        }

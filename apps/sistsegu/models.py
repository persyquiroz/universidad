from django.db import models

class opcion(models.Model):
	nombre_opcion = models.CharField(max_length=120)
	url = models.CharField(max_length=300)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre_opcion
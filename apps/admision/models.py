from django.db import models
from django import forms
import datetime

# Create your models here.
class Lugar_examen(models.Model):
	nombre_lugar = models.CharField(max_length=120)
	direccion = models.CharField(max_length=150)
	referencia = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre_lugar

class Modalidad_estudio(models.Model):
	nombre_modalidad = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_modalidad

class Modalidad_examen(models.Model):
	modalidad_examen = models.CharField(max_length=100)
	def __str__(self):
		return self.modalidad_examen

class Fechas_examen(models.Model):
	fecha_examen = models.DateField(auto_now_add =False)
	modalidad_examen = models.ForeignKey(Modalidad_examen)
	descripcion = models.TextField()
	def __str__(self):
		return self.fecha_examen.strftime('%d-%m-%Y')
		#return self.fecha_examen

class Tipo_documento(models.Model):
	nombre = models.CharField(max_length=25)
	descripcion = models.CharField("Descripción", max_length=100, null=True, blank=True, help_text="Ingrese una descripción")
	def __str__(self):
		return self.nombre

class Encuesta_examen(models.Model):
	nombres_apellidos = models.CharField("Nombres y apellidos", max_length=200, help_text="Nombres y apellidos completos")
	tipo_documento = models.ForeignKey(Tipo_documento)
	numero_doc = models.CharField("Número de documento", max_length=20, unique=True)
	edad = models.PositiveIntegerField("Edad", help_text="Ingrese sus años cumplidos")
	grado = models.CharField("Grado de estudios", max_length=100, help_text="5to grado, secundaria completa, Bachiller, etc.")
	coleg_acad_igles = models.CharField("Colegio/Academia/Iglesia", max_length=200, null=True, blank=True, help_text="Referencial")
	celular = models.CharField("N° de celular", max_length=16, help_text="Teléfono de contacto")
	correo = models.CharField("Correo electrónico", max_length=100, unique=True)
	modalidad_estudio = models.ForeignKey(Modalidad_estudio, null=True, blank=True)
	lugar_examen = models.ForeignKey(Lugar_examen)
	fechas_examen = models.ForeignKey(Fechas_examen, null=True, blank=True)
	fecha_hora_registro = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.nombres_apellidos

class Requisito(models.Model):
	nombre_requisito = models.CharField("Requisito", max_length=150, unique=True, help_text="Ingrese la descripción del requisito")
	detalles = models.TextField("Detalles", max_length=300, null=True, blank=True)
	def __str__(self):
		return self.nombre_requisito
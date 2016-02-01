from django.db import models
from apps.upeu.models import Entidad_academica

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField("Nombre", max_length=60, help_text="Nombre")
	nombres = models.CharField("Nombres", max_length=120, null=True, blank=True, help_text="Otros nombres")
	apepat = models.CharField("Apellido paterno", max_length=120)
	apemat = models.CharField("Apellido materno", max_length=120)
	fecha_nac = models.DateField("Fecha de nacimiento")
	sexo = models.CharField("Sexo", max_length=1)
	direccion = models.CharField("Dirección actual", max_length=200, null=True, blank=True)
	celular = models.CharField("Celular", max_length=12, null=True, blank=True)
	estado = models.CharField("Estado", max_length=1)
	fecha_hora_registro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s %s %s" % (self.apepat, self.apemat, self.nombre, self.nombres)

class Alumno_uni(models.Model):
	alumno = models.OneToOneField(Persona, primary_key=True)
	codigo_universitario = models.CharField("Código universitario", max_length=12, null=True, blank=True, unique=True)
	estado = models.CharField("Estado", max_length=1)
	
	def __str__(self):
		return self.codigo_universitario

class Periodo(models.Model):
	nombre_periodo = models.CharField("Nombre del periodo", max_length=30, unique=True)
	fecha_inicio = models.DateField("Fecha de inicio")
	fecha_final = models.DateField("Fecha final")
	abierto = models.CharField("Abierto", max_length=1, help_text="Use 1 parar abierto, 0 para cerrado")
	estado = models.CharField("Estado", max_length=1)
	
	def __str__(self):
		return self.nombre_periodo

class Plan_academico(models.Model):
	numero_plan = models.CharField("Número de plan", max_length=60, null=True, blank=True, unique=True)
	entidad_academica = models.ForeignKey(Entidad_academica, help_text="Escuela profesional o entidad académica")
	periodo = models.ForeignKey(Periodo, help_text="Periodo académico")
	estado = models.CharField("Estado", max_length=1)
	
	def __str__(self):
		return self.numero_plan

class Ciclo(models.Model):
	numero = models.DecimalField("Número", max_digits=2, decimal_places=0, unique=True)
	numero_letras = models.CharField("Número en letra", max_length=20, null=True, blank=True, unique=True)
	numero_romano = models.CharField("Número en romano", max_length=4, null=True, blank=True, unique=True)
	estado = models.CharField("Estado", max_length=1)

	def __str__(self):
		return "%s" % (self.numero)

class Area(models.Model):
	nombre_area = models.CharField("Nombre del área", max_length=100, unique=True)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	estado = models.CharField("Estado", max_length=1)

	def __str__(self):
		return self.nombre_area

class Curso(models.Model):
	nombre_curso = models.CharField("Nombre del curso", max_length=200)
	abreviatura = models.CharField("Abreviatura del curso", max_length=30, null=True, blank=True)
	area = models.ForeignKey(Area)
	estado = models.CharField("Estado", max_length=1)

	class Meta:
		unique_together = (('nombre_curso', 'area'),)

	def __str__(self):
		return self.nombre_curso

class Plan_acad_curso(models.Model):
	plan_academico = models.ForeignKey(Plan_academico)
	ciclo = models.ForeignKey(Ciclo)
	curso = models.ForeignKey(Curso)
	creditos = models.DecimalField("Número de créditos", max_digits=4, decimal_places=0)
	thp = models.DecimalField("THP", max_digits=4, decimal_places=0)
	hnp = models.DecimalField("HNP", max_digits=4, decimal_places=0)
	pre_requisito = models.ForeignKey('self', null=True, blank=True, help_text="Curso pre-requisito")
	estado = models.CharField("Estado", max_length=1)

	class Meta:
		unique_together = (('plan_academico', 'ciclo','curso'),)

	def __str__(self):
		return "%s (%s) %s" % (self.plan_academico, self.ciclo, self.curso)
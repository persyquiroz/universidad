from django.db import models

# Create your models here.

class Departamento(models.Model):
	  codigo = models.CharField(max_length=3, unique=True)
	  nombre_departamento = models.CharField(max_length=100, unique=True)
	  ciudad_capital = models.CharField(max_length=100, null=True, blank=True)
	  estado = models.CharField(max_length=1)
	  
	  def __str__(self):
	  	return self.nombre_departamento

class Provincia(models.Model):
	  codigo = models.CharField(max_length=6, unique=True)
	  nombre_provincia = models.CharField(max_length=100)
	  ciudad_capital = models.CharField(max_length=100, null=True, blank=True)
	  estado = models.CharField(max_length=1)
	  departamento = models.ForeignKey(Departamento)
	  
	  def __str__(self):
	  	return self.nombre_provincia

class Distrito(models.Model):
	  codigo = models.CharField(max_length=6, unique=True)
	  nombre_distrito = models.CharField(max_length=100)
	  ciudad_capital = models.CharField(max_length=100, null=True, blank=True)
	  estado = models.CharField(max_length=1)
	  provincia = models.ForeignKey(Provincia)
	  
	  def __str__(self):
	  	return self.nombre_distrito

class Tipo_universidad(models.Model):
	  descripcion = models.CharField(max_length=60, unique=True)
	  estado = models.CharField(max_length=1)
	  
	  def __str__(self):
	  	return self.descripcion

class Tipo_ent_acad(models.Model):
	  tipo_entidad = models.CharField(max_length=100, unique=True)
	  abreviatura = models.CharField(max_length=20, null=True, blank=True, unique=True)
	  conector = models.CharField(max_length=20, null=True, blank=True)
	  estado = models.CharField(max_length=1)
	  
	  def __str__(self):
	  	return self.tipo_entidad

class Entidad_academica(models.Model):
	  tipo_entidad = models.ForeignKey(Tipo_ent_acad)
	  nombre_entidad = models.CharField(max_length=100)
	  abreviatura = models.CharField(max_length=15, null=True, blank=True)
	  lugar_conocido = models.CharField(max_length=100, null=True, blank=True, help_text="Lugar de ubicacion como es conocida")
	  distrito = models.ForeignKey(Distrito, null=True, blank=True, help_text="Aplica universidad, lugar donde esta ubicada")
	  direccion = models.CharField(max_length=200, null=True, blank=True, help_text="Dirección donde está ubicada")
	  entidad_padre = models.ForeignKey('self', null=True, blank=True, help_text="A quien pertenece")
	  
	  tipo_universidad = models.ForeignKey(Tipo_universidad, null=True, blank=True, help_text="Aplica solo a universidades")
	  
	  eslogan = models.TextField(max_length=100, null=True, blank=True)
	  mision = models.TextField(max_length=2000, null=True, blank=True)
	  vision = models.TextField(max_length=2000, null=True, blank=True)
	  estado = models.CharField(max_length=1)
	  
	  def __str__(self):
	  	return self.nombre_entidad+" - "+self.lugar_conocido
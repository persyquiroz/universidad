from django.contrib import admin
from . import models
class DepartamentoAdmin(admin.ModelAdmin):
	  list_display = ["codigo", "nombre_departamento", "ciudad_capital"]
	  list_display_links = ["nombre_departamento"]
	  ordering = ['codigo']

class ProvinciaAdmin(admin.ModelAdmin):
	  list_display = ["codigo", "nombre_provincia", "ciudad_capital", "departamento"]
	  list_display_links = ["nombre_provincia"]
	  ordering = ['codigo']
	  search_fields = ["codigo","nombre_provincia"]

class DistritoAdmin(admin.ModelAdmin):
	  list_display = ["codigo", "nombre_distrito", "ciudad_capital", "provincia"]
	  list_display_links = ["nombre_distrito"]
	  ordering = ['codigo']
	  search_fields = ["codigo","nombre_distrito"]

class Tipo_ent_acadAdmin(admin.ModelAdmin):
	  list_display = ["tipo_entidad", "abreviatura", "conector"]
	  list_display_links = ["tipo_entidad"]
	  ordering = ['id']

class Entidad_academicaAdmin(admin.ModelAdmin):
	  list_display = ["abreviatura", "tipo_entidad", "nombre_entidad", "entidad_padre", "lugar_conocido", "distrito", "direccion"]
	  list_display_links = ["nombre_entidad"]
	  ordering = ['tipo_entidad', '-entidad_padre','id']

admin.site.register(models.Departamento, DepartamentoAdmin),
admin.site.register(models.Provincia, ProvinciaAdmin),
admin.site.register(models.Distrito, DistritoAdmin),
admin.site.register(models.Tipo_universidad),
admin.site.register(models.Tipo_ent_acad, Tipo_ent_acadAdmin),
admin.site.register(models.Entidad_academica, Entidad_academicaAdmin),
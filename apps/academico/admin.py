from django.contrib import admin
from . import models
# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
	  list_display = ["alumno", "codigo_universitario"]
	  list_display_links = ["alumno"]

class PeriodoAdmin(admin.ModelAdmin):
	  list_display = ["nombre_periodo", "fecha_inicio", "fecha_final"]
	  list_display_links = ["nombre_periodo"]
	  ordering = ['fecha_inicio']

class Plan_academicoAdmin(admin.ModelAdmin):
	  list_display = ["numero_plan", "entidad_academica", "periodo"]
	  list_display_links = ["numero_plan"]
	  ordering = ['numero_plan']

class CicloAdmin(admin.ModelAdmin):
	  list_display = ["numero", "numero_letras", "numero_romano"]
	  list_display_links = ["numero","numero_letras"]
	  ordering = ['numero']

class CursoAdmin(admin.ModelAdmin):
	  list_display = ["nombre_curso", "abreviatura", "area"]
	  list_display_links = ["nombre_curso"]
	  ordering = ['id']

class Plan_acad_cursoAdmin(admin.ModelAdmin):
	  list_display = ["plan_academico", "ciclo", "curso", "creditos", "thp", "hnp", "pre_requisito"]
	  list_display_links = ["curso"]
	  ordering = ['plan_academico','ciclo','id']

admin.site.register(models.Persona),
admin.site.register(models.Alumno_uni, AlumnoAdmin),
admin.site.register(models.Periodo, PeriodoAdmin),
admin.site.register(models.Plan_academico, Plan_academicoAdmin),
admin.site.register(models.Ciclo, CicloAdmin),
admin.site.register(models.Area),
admin.site.register(models.Curso, CursoAdmin),
admin.site.register(models.Plan_acad_curso, Plan_acad_cursoAdmin),
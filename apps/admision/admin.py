from django.contrib import admin
from . import models
# Register your models here.
class Lugar_examenAdmin(admin.ModelAdmin):
      list_display = ["nombre_lugar","direccion","referencia"]

class Fechas_examenAdmin(admin.ModelAdmin):
      list_display = ["fecha_examen","modalidad_examen","descripcion"]

class Tipo_docAdmin(admin.ModelAdmin):
      list_display = ["nombre","descripcion"]

class Encuesta_examenAdmin(admin.ModelAdmin):
	  list_display = ["lugar_examen", "fechas_examen", "nombres_apellidos", "tipo_documento", "numero_doc", "edad", "celular", "correo"]
	  list_display_links = ["nombres_apellidos"]
	  ordering = ['lugar_examen', 'fechas_examen','nombres_apellidos']
	  #list_editable = ["nombres_apellidos", "fechas_examen"]
      #search_fields = ["nombre_religion"]

class RequisitoAdmin(admin.ModelAdmin):
	  list_display = ["id", "nombre_requisito", "detalles"]
	  list_display_links = ["id", "nombre_requisito"]
	  ordering = ['id']

admin.site.register(models.Lugar_examen, Lugar_examenAdmin),
admin.site.register(models.Modalidad_estudio),
admin.site.register(models.Modalidad_examen),
admin.site.register(models.Fechas_examen, Fechas_examenAdmin),
admin.site.register(models.Tipo_documento, Tipo_docAdmin),
admin.site.register(models.Encuesta_examen, Encuesta_examenAdmin),
admin.site.register(models.Requisito, RequisitoAdmin),
from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^alumnos_uni/$', views.Listar_alumnos_uni.as_view(), name="listar_alumnos_uni"),
   url(r'^alumnos_uni/agregar/$', views.Registrar_persona_alumno.as_view(), name="agregar_persona"),
   url(r'^alumnos_uni/agregar_alumno/(?P<pk>\d+)/$', views.Registrar_alumno.as_view(), name="agregar_alumno"),
   url(r'^alumnos_uni/actualizar_alumno/(?P<pk>\d+)/$', views.Actualizar_alumno.as_view(), name="actualizar_alumno"),
   url(r'^periodos/$', views.Listar_periodos.as_view(), name="listar_periodos"),
   url(r'^planes_academicos/$', views.Listar_planes_academicos.as_view(), name="listar_planes_academicos"),
   url(r'^planes_academicos_cursos/$', views.BusquedaPlan_acad_curso),
   url(r'^planes_academicos_cursos/agregar/$', views.Nuevo_plan_acad_curso, name="lista_agregar_plan_curso"),
   url(r'^planes_academicos_cursos/buscar_facultad/', views.Buscar_facultad),
   url(r'^planes_academicos_cursos/buscar_escuela/', views.Buscar_escuela),
   url(r'^planes_academicos_cursos/buscar_plan_acad/', views.Buscar_plan_acad),
   url(r'^planes_academicos_cursos/buscar_plan_acad_cursos/', views.Listado_plan_acad_cursos),
   url(r'^planes_academicos_cursos/nuevo_plan_curso/', views.Nuevo_plan_curso),
   url(r'^planes_academicos_cursos/buscar_curso_plan/', views.Buscar_curso_plan),
   url(r'^planes_academicos_cursos/agregar_plan_acad_curso/', views.Agregar_plan_acad_curso2),
   url(r'^planes_academicos_cursos/buscar_pre_requisito/', views.Buscar_pre_requisito),
   url(r'^planes_academicos_cursos/eliminar_plan_acad_curso/', views.Eliminar_plan_acad_curso),
   url(r'^planes_academicos_cursos/nuevo_curso/', views.Nuevo_curso),
   url(r'^planes_academicos_cursos/guardar_curso/', views.Guardar_curso),
   url(r'^planes_academicos_cursos/editar_plan_curso/', views.Editar_plan_curso),

   ]
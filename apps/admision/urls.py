from django.conf.urls import url
#from .views import Listar_lugar_examen, Registrar_lugar_examen, Actualizar_lugar_examen, Listar_requisitos, Eliminar_lugar_examen, Listar_encuestas_examen, Listar_encuestas_examen_imp, Registrar_encuesta_examen, Actualizar_encuesta_examen
#from .views import Eliminar_encuesta_examen, ver_impresion_encuesta, Detalle_encuestas_examen
#Reporte1
from . import views
urlpatterns = [
   url(r'^lugares_examen/$', views.Listar_lugar_examen.as_view(), name="listar_lugares_examen"),
   url(r'^lugares_examen/nuevo/$', views.Registrar_lugar_examen.as_view(), name="nuevo_lugar_examen"),
   url(r'^lugares_examen/editar/(?P<pk>\d+)/$', views.Actualizar_lugar_examen.as_view(), name="editar_lugar_examen"),
   url(r'^lugares_examen/eliminar/(?P<pk>\d+)/$', views.Eliminar_lugar_examen.as_view(), name="eliminar_lugar_examen"),
   url(r'^requisitos/$', views.Listar_requisitos.as_view(), name="listar_requisitos"),
   url(r'^encuestas_examen/$', views.Listar_encuestas_examen.as_view(), name="listar_encuestas_examen"),
   url(r'^encuestas_examen/detalle/(?P<pk>\d+)/$', views.Detalle_encuestas_examen.as_view(), name="detalle_encuesta_examen"),
   url(r'^encuestas_examen/impresion/$', views.Listar_encuestas_examen_imp.as_view(), name="listar_encuestas_examen_imp"),
   url(r'^encuestas_examen/nueva/$', views.Registrar_encuesta_examen.as_view(), name="nuevo_encuesta_examen"),
   url(r'^encuestas_examen/editar/(?P<pk>\d+)/$', views.Actualizar_encuesta_examen.as_view(), name="editar_encuesta_examen"),
   url(r'^encuestas_examen/eliminar/(?P<pk>\d+)/$', views.Eliminar_encuesta_examen.as_view(), name="eliminar_encuesta_examen"),
   url(r'^encuestas_examen/ver_impresion/$', views.ver_impresion_encuesta),
   url(r'^encuestas_examen/reporte1/$', views.Reporte1)
   ]

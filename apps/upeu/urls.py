from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.pagina_inicio),
  url(r'^login/$', views.login_inicial),
  url(r'^logout/$', views.cerrar_sesion),
]
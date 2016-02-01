from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from .models import Lugar_examen, Requisito, Encuesta_examen
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
# Create your views here.
def Reporte1(request):
	hola = "Hola  a todos"
	encuestados = Encuesta_examen.objects.all()

	lugares = Lugar_examen.objects.filter(id__in=Encuesta_examen.objects.values('lugar_examen_id').distinct())
	
	return render_to_response('admision/encuesta_examen/reporte1.html',{'lugares':lugares,'encuestados':encuestados,'hola':hola})

class Listar_lugar_examen(ListView):
	template_name='admision/lugar_examen/index.html'
	model= Lugar_examen
	context_object_name = 'lugares_examen'

class Registrar_lugar_examen(CreateView):
	template_name='admision/lugar_examen/form_new.html'
	model = Lugar_examen
	fields = ['nombre_lugar','direccion','referencia']
	success_url = reverse_lazy('listar_lugares_examen')

class Actualizar_lugar_examen(UpdateView):
	template_name = 'admision/lugar_examen/form_update.html'
	model = Lugar_examen
	fields = ['nombre_lugar','direccion','referencia']
	success_url = reverse_lazy('listar_lugares_examen')

class Eliminar_lugar_examen(DeleteView):
	template_name = 'admision/lugar_examen/eliminar.html'
	model = Lugar_examen
	success_url = reverse_lazy('listar_lugares_examen')

class Listar_requisitos(ListView):
	template_name='admision/requisito/index.html'
	model= Requisito
	context_object_name = 'requisitos'
	def get_queryset(self):
   		return Requisito.objects.order_by('id')

class Listar_encuestas_examen(ListView):
	template_name='admision/encuesta_examen/index.html'
	model= Encuesta_examen
	context_object_name = 'encuestas_examen'
	def get_queryset(self):
   		return Encuesta_examen.objects.order_by('fechas_examen','lugar_examen','nombres_apellidos')

class Listar_encuestas_examen_imp(ListView):
	template_name='admision/encuesta_examen/impresion.html'
	model= Encuesta_examen
	context_object_name = 'encuestas_examen'
	def get_queryset(self):
   		return Encuesta_examen.objects.order_by('fechas_examen','lugar_examen','nombres_apellidos')

class Detalle_encuestas_examen(DetailView):
	model = Encuesta_examen
	context_object_name = 'encuesta'
	template_name = 'admision/encuesta_examen/detalle.html'

class Registrar_encuesta_examen(SuccessMessageMixin, CreateView):
	template_name='admision/encuesta_examen/form_new.html'
	model = Encuesta_examen
	fields = ['nombres_apellidos','tipo_documento','numero_doc','edad','grado','coleg_acad_igles',
			 'celular','correo','modalidad_estudio','lugar_examen','fechas_examen','fecha_hora_registro']
	success_message = "La encuesta para examen registrada de: %(nombres_apellidos)s"
	#success_url = reverse_lazy('listar_encuestas_examen')
	def get_success_url(self):
		return reverse('detalle_encuesta_examen', kwargs={'pk': self.object.pk})

class Actualizar_encuesta_examen(SuccessMessageMixin, UpdateView):
	template_name='admision/encuesta_examen/form_update.html'
	model = Encuesta_examen
	fields = ['nombres_apellidos','tipo_documento','numero_doc','edad','grado','coleg_acad_igles',
			 'celular','correo','modalidad_estudio','lugar_examen','fechas_examen','fecha_hora_registro']
	success_message = "La encuesta para examen actualizada de: %(nombres_apellidos)s"
	#success_url = reverse_lazy('listar_encuestas_examen')
	def get_success_url(self):
		return reverse('detalle_encuesta_examen', kwargs={'pk': self.object.pk})

class Eliminar_encuesta_examen(SuccessMessageMixin, DeleteView):
	template_name = 'admision/encuesta_examen/eliminar.html'
	model = Encuesta_examen
	fields = ['nombres_apellidos']
	success_message = "La encuesta para examen eliminada de: %(nombres_apellidos)s"
	success_url = reverse_lazy('listar_encuestas_examen')

def ver_impresion_encuesta(request):
	return render(request,'admision/encuesta_examen/ver_impresion.html')
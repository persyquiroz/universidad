from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Alumno_uni, Persona, Alumno_uni, Periodo, Plan_academico, Plan_acad_curso, Ciclo, Curso, Area
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum, F, Q
from apps.upeu.models import Entidad_academica

# Create your views here.
class Listar_alumnos_uni(ListView):
	template_name='academico/alumno_uni/index.html'
	model= Alumno_uni
	context_object_name = 'alumnos_uni'

class Registrar_persona1(CreateView):
	template_name='academico/alumno_uni/form_new.html'
	model = Persona
	fields = ['nombre','nombres','apepat','apemat','fecha_nac','sexo','direccion','celular','estado']
	def get_success_url(self):
		return reverse('agregar_alumno', kwargs={'pk': self.object.pk})

class Registrar_persona_alumno(CreateView):
	template_name='academico/alumno_uni/form_new.html'
	model = Persona
	fields = ['nombre','nombres','apepat','apemat','fecha_nac','sexo','direccion','celular','estado']
	def get_success_url(self):
		print ("Hola a todos")
		alu = Alumno_uni(alumno_id=self.object.pk,
								estado='1')
		alu.save()

		return reverse('actualizar_alumno', kwargs={'pk': self.object.pk})

class Registrar_alumno(CreateView):
	template_name='academico/alumno_uni/form_new_alumno.html'
	model = Alumno_uni
	fields = ['alumno', 'codigo_universitario','estado']
	success_url = reverse_lazy('listar_alumnos_uni')


class Actualizar_alumno(UpdateView):
	template_name = 'academico/alumno_uni/form_new_alumno.html'
	model = Alumno_uni
	fields = ['codigo_universitario','estado']
	success_url = reverse_lazy('listar_alumnos_uni')

class Listar_periodos(ListView):
	template_name='academico/periodo/index.html'
	model= Periodo
	context_object_name = 'periodos'

class Listar_planes_academicos(ListView):
	template_name='academico/plan_academico/index.html'
	model= Plan_academico
	context_object_name = 'planes_academicos'

def BusquedaPlan_acad_curso(request):
	hola = "Hola  a todos"
	if request.method == 'POST':
		plan_academico = request.POST['plan_academico']
		
	else:
		plan_academico = '0'


	planes_academicos = Plan_academico.objects.all()
	planes_acad_cursos = Plan_acad_curso.objects.filter(plan_academico=plan_academico).annotate(total_horas=F('thp') + F('hnp')).order_by('ciclo')
	
	ciclos = Ciclo.objects.filter(id__in=Plan_acad_curso.objects.values('ciclo_id').distinct().filter(plan_academico=plan_academico)).order_by('numero')

	context = {'ciclos':ciclos, 'plan_academico':plan_academico, 'planes_acad_cursos':planes_acad_cursos, 'hola':hola, 'planes_academicos':planes_academicos}
	
	return render_to_response('academico/plan_acad_curso/index.html', context, context_instance=RequestContext(request))

def Nuevo_plan_acad_curso(request):
	list_ent_univers = Entidad_academica.objects.filter(tipo_entidad=1).order_by('tipo_entidad')

	context = {'list_ent_univers':list_ent_univers}
	#return render(request,'upeu/index.html')
	return render(request, 'academico/plan_acad_curso/form_new.html', context)

def Buscar_facultad(request):
	if request.GET:
		id_univers = request.GET['id_univers']
		list_ent_facultades = Entidad_academica.objects.filter(tipo_entidad=2, entidad_padre=id_univers).order_by('nombre_entidad')
		context = {'list_ent_facultades':list_ent_facultades}
		return render(request, 'academico/plan_acad_curso/busq/busq_facultad.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/busq/busq_facultad.html')

def Buscar_escuela(request):
	if request.GET:
		id_facultad = request.GET['id_facultad']
		list_ent_escuelas = Entidad_academica.objects.filter(tipo_entidad=3, entidad_padre=id_facultad).order_by('nombre_entidad')
		context = {'list_ent_escuelas':list_ent_escuelas}
		return render(request, 'academico/plan_acad_curso/busq/busq_escuela.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/busq/busq_escuela.html')

def Buscar_plan_acad(request):
	if request.GET:
		id_escuela = request.GET['id_escuela']
		list_planes_acad = Plan_academico.objects.filter(entidad_academica=id_escuela)
		context = {'list_planes_acad':list_planes_acad}
		return render(request, 'academico/plan_acad_curso/busq/busq_plan_acad.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/busq/busq_plan_acad.html')

def Listado_plan_acad_cursos(request):
	if request.GET:
		plan_academico = request.GET['id_plan_academico']
		
	else:
		plan_academico = '0'


	planes_acad_cursos = Plan_acad_curso.objects.filter(plan_academico=plan_academico).annotate(total_horas=F('thp') + F('hnp')).order_by('ciclo')
	
	ciclos = Ciclo.objects.filter(id__in=Plan_acad_curso.objects.values('ciclo_id').distinct().filter(plan_academico=plan_academico)).order_by('numero')

	context = {'ciclos':ciclos, 'planes_acad_cursos':planes_acad_cursos}
	
	return render(request, 'academico/plan_acad_curso/busq/busq_plan_acad_cursos.html',context)
	
	

def Nuevo_plan_curso(request):
	if request.GET:
		id_plan_academico = request.GET['id_plan_academico']
		
		lista_ciclos = Ciclo.objects.all().order_by('numero')
		plan_academico = Plan_academico.objects.filter(id=id_plan_academico)
		
		#planes_acad_cursos = Plan_acad_curso.objects.filter(plan_academico=id_plan_academico).annotate(total_horas=F('thp') + F('hnp')).order_by('ciclo')
		#ciclos = Ciclo.objects.filter(id__in=Plan_acad_curso.objects.values('ciclo_id').distinct().filter(plan_academico=id_plan_academico)).order_by('numero')

		context = {'lista_ciclos':lista_ciclos, 'plan_academico':plan_academico}

		return render(request, 'academico/plan_acad_curso/form_new_plan_curso.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/form_new_plan_curso.html')


def Buscar_curso_plan(request):
	if request.GET:
		buscar = request.GET['buscar']
		plan_academico = request.GET['plan_academico']
		print (buscar)
		lista_cursos = Curso.objects.filter(nombre_curso__icontains=buscar).exclude(id__in=Plan_acad_curso.objects.values('curso_id').distinct().filter(plan_academico=plan_academico)).order_by('nombre_curso')[:8]
		context = {'Hola':"123", 'lista_cursos':lista_cursos}

		return render(request, 'academico/plan_acad_curso/busq/busq_curso.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/busq_curso.html')

def Agregar_plan_acad_curso(request):
	if request.method == 'POST':
		plan_academico = request.POST['plan_academico']
		ciclo = request.POST['ciclo']
		curso = request.POST['curso']
		creditos = request.POST['creditos']
		thp = request.POST['thp']
		hnp = request.POST['hnp']
		pre_requisito = request.POST['pre_requisito']
		
		p = Plan_acad_curso(plan_academico_id=plan_academico,
								ciclo_id=ciclo,
								curso_id=curso,
								creditos=creditos,
								thp=thp,
								hnp=hnp,
								pre_requisito_id=pre_requisito,
								estado='1')
		p.save()
		if p.save:
			resultado = "Registrado correctamente"
			list_ent_univers = Entidad_academica.objects.filter(tipo_entidad=1).order_by('tipo_entidad')
			context = {'resultado':resultado, 'list_ent_univers':list_ent_univers}
			return render(request, 'academico/plan_acad_curso/form_new.html', context)
		
		else:
			resultado = "No se pudo registrar"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/form_new.html', context)	

	else:
		resultado = "No envió un método POST"
		context = {'resultado':resultado}
		return reverse(request, 'academico/plan_acad_curso/form_new.html', context)

def Agregar_plan_acad_curso2(request):
	if request.method == 'GET':
		plan_academico = request.GET['plan_academico']
		ciclo = request.GET['ciclo']
		curso = request.GET['curso']
		creditos = request.GET['creditos']
		thp = request.GET['thp']
		hnp = request.GET['hnp']
		pre_requisito = request.GET['pre_requisito']
		try:
			p = Plan_acad_curso(plan_academico_id=plan_academico,
								ciclo_id=ciclo,
								curso_id=curso,
								creditos=creditos,
								thp=thp,
								hnp=hnp,
								pre_requisito_id=pre_requisito,
								estado='1')
			p.save()
			#if p.save:
			resultado = "Registrado correctamente"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resultado_agregar_plan_curso.html', context)
		
		except:
			resultado = "No se pudo registrar, ingrese todos los datos requeridos, no duplique un curso existente"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resultado_agregar_plan_curso.html', context)	

	else:
		resultado = "No envió un método POST"
		context = {'resultado':resultado}
		return reverse(request, 'academico/plan_acad_curso/busq/resultado_agregar_plan_curso.html', context)


def Buscar_pre_requisito(request):
	if request.GET:
		id_plan_academico = request.GET['id_plan_academico']
		buscar = request.GET['buscar']
		ciclo = int(request.GET['ciclo'])
		# Para mayores se usa __gt (>) y para menor:__lt
		planes_acad_cursos = Plan_acad_curso.objects.filter(plan_academico=id_plan_academico, curso__nombre_curso__icontains=buscar, 
															ciclo_id__lt=ciclo).order_by('curso')

		context = {'planes_acad_cursos':planes_acad_cursos}

		return render(request, 'academico/plan_acad_curso/busq/busq_pre_requisito.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/busq/busq_pre_requisito.html')

def Eliminar_plan_acad_curso(request):
	if request.GET:
		academico_plan_acad_curso = request.GET['academico_plan_acad_curso']
		try:
			plan = Plan_acad_curso.objects.get(pk=academico_plan_acad_curso)
			plan.delete()

			resultado = "Eliminado correctamente"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resul_eliminar_curso.html', context)

		except:
			resultado = "No se pudo eliminar curso"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resul_eliminar_curso.html', context)	

	else:
		resultado = "Ninguna acción realizado"
		context = {'resultado':resultado}
		return render(request, 'academico/plan_acad_curso/busq/resul_eliminar_curso.html', context)	

def Nuevo_curso(request):
	lista_areas = Area.objects.all()
	context = {'lista_areas':lista_areas}
	return render(request, 'academico/curso/new_curso_exterior.html', context)

def Guardar_curso(request):
	if request.method == 'GET':
		nombre_curso = request.GET['nombre_curso']
		area = request.GET['area']
		abreviatura = request.GET['abreviatura']
		try:
			c = Curso(nombre_curso=nombre_curso,
								area_id=area,
								abreviatura=abreviatura,
								estado='1')
			c.save()
			c.id
			print (c.id)
			#if p.save:
			resultado = "Registrado correctamente"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resul_reg_curso.html', context)
		
		except:
			resultado = "No se pudo registrar, complete los campos"
			context = {'resultado':resultado}
			return render(request, 'academico/plan_acad_curso/busq/resul_reg_curso.html', context)	

	else:
		resultado = "No envió un método GET"
		context = {'resultado':resultado}
		return reverse(request, 'academico/plan_acad_curso/busq/resul_reg_curso.html', context)


def Editar_plan_curso(request):
	if request.GET:
		id_plan_academico = request.GET['id_plan_academico']
		
		lista_ciclos = Ciclo.objects.all().order_by('numero')
		plan_academico = Plan_academico.objects.filter(id=id_plan_academico)
		
		#planes_acad_cursos = Plan_acad_curso.objects.filter(plan_academico=id_plan_academico).annotate(total_horas=F('thp') + F('hnp')).order_by('ciclo')
		#ciclos = Ciclo.objects.filter(id__in=Plan_acad_curso.objects.values('ciclo_id').distinct().filter(plan_academico=id_plan_academico)).order_by('numero')

		context = {'lista_ciclos':lista_ciclos, 'plan_academico':plan_academico}

		return render(request, 'academico/plan_acad_curso/form_new_plan_curso.html',context)
	else:
		return render(request, 'academico/plan_acad_curso/form_new_plan_curso.html')


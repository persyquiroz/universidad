from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden, HttpResponseRedirect


def pagina_inicio(request):
	return render(request,'upeu/index.html')

def login_inicial(request):

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				mensaje = "Bienvenido "+ username +" al sistema"
				# Redirect to a success page.
				return render(request,'upeu/index.html')
			else:
				# Return a 'disabled account' error message
				mensaje = "El usuario está desactivo"
				return render(request,'upeu/index.html', {'mensaje':mensaje})
		else:
			# Return an 'invalid login' error message.
			mensaje = username +", su identificación es incorrecta, vuelva a intentar nuevamente."
			#return render_to_response('admision/encuesta_examen/reporte1.html',{'lugares':lugares,'encuestados':encuestados,'hola':hola})
			return render(request,'upeu/index.html', {'mensaje':mensaje})	
	else:
# Return an 'invalid login' error message.
		#raise SuspiciousOperation
		#return HttpResponseForbidden()
		return render(request,'upeu/index.html')

def cerrar_sesion(request):
	logout(request)
	mensaje = "Sesión cerrada"
	return render(request,'upeu/index.html', {'mensaje':mensaje})	
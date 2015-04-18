from django.shortcuts import render_to_response, render
from forms import Datos_publicados
from django.http import HttpResponseRedirect, Http404
from django.core.context_processors import csrf
from django.db.models import Q
from models import Datos
from django import forms
from django.views import generic
import models



def Ingresando_datos(request):
	if request.method == 'POST':
		form = Datos_publicados(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Ingresando_datos')
	else:
		form = Datos_publicados()
	c = {'form':form}
	c.update(csrf(request))
	return render_to_response('Ingresando_datos.html', c)
	
def Buscar(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(Lenguaje__icontains=query)
		)
		results = Datos.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("buscar.html", { "results":results, "query": query})

def qu(request, dato_id):
	try:
		dato = Datos.objects.get(pk=dato_id)
	except Datos.DoesNotExist:
		raise Http404
	return render(request, 'contenido.html', {'dato':dato})

class Data(generic.ListView):
	template_name = 'article-list.html'
	context_object_name = 'Datos_list'
	def get_queryset(self):
		return Datos.objects.order_by('-id').reverse()




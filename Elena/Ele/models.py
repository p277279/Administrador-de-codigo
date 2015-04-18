from django.db import models
from django.core.validators import MaxLengthValidator
import datetime
from django import forms

class Datos(models.Model):
	Nombre = models.CharField(max_length = 30)
	Autor = models.CharField(max_length = 30)
	Lenguaje = models.CharField(max_length = 15)
	Descripcion = models.CharField(max_length = 60)
	Codigo = models.TextField(validators=[MaxLengthValidator(10000)])
	Fecha = models.DateField()

	def __str__(self):
		return 'Nombre: [ %s ] | Autor:[ %s ] | Lenguaje:[ %s ] | Descripcion:[ %s ] | Fecha:[ %s ] | Codigo:[ %s ]' % (self.Nombre, self.Autor,self.Lenguaje,self.Descripcion,self.Fecha,self.Codigo)

	

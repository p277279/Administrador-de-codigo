from models import Datos
from django.forms import ModelForm


class Datos_publicados(ModelForm):
	class Meta:
		model = Datos
		




from django.forms import ModelForm

from .models import *


class OwnerForm(ModelForm):
	class Meta:
		model = Owner
		fields = '__all__'


class CarForm(ModelForm):
	class Meta:
		model = Car
		fields = '__all__'

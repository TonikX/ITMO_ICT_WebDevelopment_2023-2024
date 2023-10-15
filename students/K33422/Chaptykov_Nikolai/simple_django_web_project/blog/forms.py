from django import forms
from .models import ExampleModel, Person, Car
from django.contrib.auth.models import User
  

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
  
        fields = [
            "title",
            "description",
        ]


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
  
        fields = [
            "first_name",
            "last_name",
            "birthdate",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
  
        fields = [
            'plate_number',
            'company_produced',
            'model',
            'color',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name',)
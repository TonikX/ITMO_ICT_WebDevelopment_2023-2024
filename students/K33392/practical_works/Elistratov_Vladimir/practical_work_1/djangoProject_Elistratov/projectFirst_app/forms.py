from django import forms
from .models import CarOwner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creating a form
class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "username",
            "password",
            "firstName",
            "lastName",
            "bornDate",
            "passportNumber",
            "passportSubNumber",
        ]
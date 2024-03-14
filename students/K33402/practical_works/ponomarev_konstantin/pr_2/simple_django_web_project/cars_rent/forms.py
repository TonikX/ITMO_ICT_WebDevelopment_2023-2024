from django import forms
from .models import Driver, Car


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
            "birth_date",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "number",
            "brand",
            "model",
            "color",
        ]

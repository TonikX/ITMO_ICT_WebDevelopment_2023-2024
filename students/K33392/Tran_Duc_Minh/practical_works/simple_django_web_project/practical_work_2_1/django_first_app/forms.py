from django import forms
from .models import Owner, Car

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
        ]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "state_number",
            "brand",
            "model",
            "color",
        ]
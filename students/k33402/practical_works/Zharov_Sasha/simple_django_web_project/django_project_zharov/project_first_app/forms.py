from django import forms
from .models import Driver


# creating a form
class DriverForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Driver

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CarOwner, CustomUser


# creating a form
class CarOwnerForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = CarOwner

        # specify fields to be used
        fields = [
            "first_name",
            "last_name",
            "date_of_birth"
        ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "passport_number",
            "home_address",
            "nationality",
        )

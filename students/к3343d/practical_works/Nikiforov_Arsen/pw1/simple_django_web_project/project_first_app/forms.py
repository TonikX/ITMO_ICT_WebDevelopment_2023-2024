from django import forms
from .models import ExampleModel
from .models import Owner
from .models import Car
from .models import CustomUser, OwnerProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'passport_number', 'home_address', 'nationality']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        



class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'  # Это позволит использовать все поля модели Owner












class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = [
            "title",
            "description",
        ]

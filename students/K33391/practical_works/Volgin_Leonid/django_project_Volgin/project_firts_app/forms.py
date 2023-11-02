from django import forms
from .models import CarOwner
class CarOwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ["first_name", "surname", "date_of_birth"]
        labels = {
            "first_name": "Имя",
            "surname": "Фамилия",
            "date_of_birth": "Дата рождения",

        }


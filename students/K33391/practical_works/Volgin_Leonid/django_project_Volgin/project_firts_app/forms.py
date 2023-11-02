from django import forms
from .models import CarOwner, Car
class CarOwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ["first_name", "surname", "date_of_birth"]
        labels = {
            "first_name": "Имя",
            "surname": "Фамилия",
            "date_of_birth": "Дата рождения",

        }
class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["number", "brand", "model", "color"]
        labels = {
            "number": "Номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["number", "brand", "model", "color"]
        labels = {
            "number": "Номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }

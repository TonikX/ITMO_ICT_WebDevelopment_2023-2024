from django import forms
from .models import Car, CarOwner


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number", "brand", "model", "color"]
        labels = {
            "state_number": "Номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number", "brand", "model", "color"]
        labels = {
            "state_number": "Номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }


class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ["surname", "name", "birth_date"]
        labels = {
            "surname": "Фамилия",
            "name": "Имя",
            "birth_date": "Дата рождения",
        }
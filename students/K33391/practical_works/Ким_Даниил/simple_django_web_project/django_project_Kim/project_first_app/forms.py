from django import forms
from .models import *


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "second_name",
            "birthday",
            "passport",
            "address",
            "nationality",
        ]

        labels = {
            "first_name": "Имя",
            "second_name": "Фамилия",
            "birthday": "Дата Рождения",
            "passport": "Номер паспорта",
            "address": "Адрес",
            "nationality": "Национальности",
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car

        fields = [
            'state_number',
            'brand',
            'model',
            'color'
        ]

        labels = {
            "state_number": "Гос номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number",
                  "brand",
                  "model",
                  "color"]

        labels = {
            "state_number": "Гос номер",
            "brand": "Марка",
            "car_model": "Модель",
            "color": "Цвет",
        }
from django import forms
from .models import CarOwner, Car


class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ["username", "password", "first_name", "last_name", "birthday_date", "passport", "address",
                  "nationality"]
        labels = {
            "username": "Логин",
            "password": "Пароль",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "birthday_date": "Дата рождения",
            "passport": "Паспорт",
            "address": "Адрес",
            "nationality": "Национальность"
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

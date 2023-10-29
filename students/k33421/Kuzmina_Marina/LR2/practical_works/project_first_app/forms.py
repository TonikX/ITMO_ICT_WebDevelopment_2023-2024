from django import forms
from .models import Driver, Car


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['username', 'password', 'first_name', 'last_name', 'date_of_birth',
                  'passport_number', 'address', 'nationality']
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'date_of_birth': 'Дата рождения',
            'passport_number': 'Паспорт',
            'address': 'Адрес',
            'nationality': 'Национальность',
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number', 'brand', 'car_model', 'color']
        labels = {
            'number': 'Номер',
            'brand': 'Марка',
            'car_model': 'Модель',
            'color': 'Цвет',
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number', 'brand', 'car_model', 'color']
        labels = {
            'number': 'Номер',
            'brand': 'Марка',
            'car_model': 'Модель',
            'color': 'Цвет',
        }

from django import forms
from .models import Driver, Auto


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['username', 'password', 'first_name', 'last_name', 'birth_date',
                  'passport', 'address', 'nationality']
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'birth_date': 'Дата рождения',
            'passport': 'Паспорт',
            'address': 'Адрес',
            'nationality': 'Национальность',
        }


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['state_number', 'brand', 'model', 'color']
        labels = {
            'state_number': 'Госномер',
            'brand': 'Марка',
            'model': 'Модель',
            'color': 'Цвет',
        }

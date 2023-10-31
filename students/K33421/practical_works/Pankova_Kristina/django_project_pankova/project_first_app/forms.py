from django import forms
from .models import CarOwner


# creating a form
class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'birth_date',
                  'passport',
                  'address',
                  'nationality'
                  ]
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

from django import forms
from .models import Driver
  

class DriverForm(forms.ModelForm):
  
    class Meta:
        model = Driver
        
        fields = ['username', 
                  'password', 
                  'first_name', 
                  'last_name', 
                  'birthdate',
                  'passport_number', 
                  'address', 
                  'nationality']
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'birthdate': 'Дата рождения',
            'passport_number': 'Паспорт',
            'address': 'Адрес',
            'nationality': 'Национальность',
        }
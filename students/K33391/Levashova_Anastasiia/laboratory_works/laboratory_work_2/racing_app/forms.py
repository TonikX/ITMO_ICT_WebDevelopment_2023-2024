from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from racing_app.models import Racer, RacerCar


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class RacerProfileForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['first_name', 'last_name', 'team_name', 'participant_description', 'experience']
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "team_name": "Название команды",
            "participant_description": "Описание",
            "experience": "Опыт (лет)",
        }


class RacerCarForm(forms.ModelForm):
    class Meta:
        model = RacerCar
        fields = ['state_number', 'brand', 'model', 'color']
        labels = {
            "state_number": "Номер",
            "brand": "Марка",
            "model": "Модель",
            "color": "Цвет",
        }

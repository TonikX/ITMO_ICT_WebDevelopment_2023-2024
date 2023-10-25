from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Ticket


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "passport",
        ]
        labels = {
            "username": "Логин",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "date_of_birth": "Дата рождения",
            "passport": "Паспорт",
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "seat",
        ]
        labels = {
            "seat": "Место",
        }

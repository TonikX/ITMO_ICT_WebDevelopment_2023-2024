from django import forms
from .models import CarOwner, Car
class CarOwnerCreateForm(forms.ModelForm):
     class Meta:
         model = CarOwner
         fields = ["username","password","first_name", "surname", "date_of_birth","passport","address","nationality"]
         labels = {
             "username": "Логин",
             "password": "Пароль",
             "first_name": "Имя",
             "surname": "Фамилия",
             "date_of_birth": "Дата рождения",
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

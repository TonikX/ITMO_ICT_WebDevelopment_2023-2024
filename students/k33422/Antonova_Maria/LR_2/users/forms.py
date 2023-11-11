from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm): #наследует функционал формы UserCreationForm
    first_name = forms.CharField(required=True) #Добавление двух полей first_name и last_name для имени и фамилии пользователей/Оба поля устанавливаются как обязательные к заполнению
    last_name = forms.CharField(required=True)

    class Meta:
        model = User #на основе модели User (встроенной модели пользователя Django)
        fields = ['username', 'first_name', 'last_name','password1', 'password2'] #username (имя пользователя), first_name (имя), last_name (фамилия), password1 (пароль) и password2 (подтверждение пароля)
    
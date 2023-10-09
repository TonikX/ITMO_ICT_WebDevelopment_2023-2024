from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *


class StudentRegistrationForm(UserCreationForm):
    fio = forms.CharField(
        max_length=250,
        required=True,
        help_text="Введите ваше ФИО (через пробел)"
    )
    student_class = forms.ModelChoiceField(
        queryset=Class.objects.filter(date_to__gte=date.today()),
        required=True,
        empty_label="Выберите ваш класс"
    )
    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        required=False,
    )
    address = forms.CharField(
        max_length=250,
        required=False,
        help_text="Введите ваш адрес (не обязательно)"
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'fio', 'student_class', 'date_of_birth', 'address']
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
            'fio': 'ФИО',
            'student_class': 'Класс',
            'date_of_birth': 'Дата рождения',
            'address': 'Адрес',
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fio', 'date_of_birth', 'address']
        labels = {
            'fio': 'ФИО',
            'date_of_birth': 'Дата рождения',
            'address': 'Адрес',
        }


class HomeworkSubmissionForm(forms.ModelForm):
    class Meta:
        model = HomeworkSubmission
        fields = ['submission_text']
        labels = {'submission_text': 'Текст ответа'}


class HomeworkForm(forms.ModelForm):
    class_it_is_assigned_to = forms.ModelChoiceField(
        queryset=Class.objects.filter(date_to__gte=date.today()),
        required=True,
    )

    deadline_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        required=False,
    )

    class Meta:
        model = Homework
        fields = ['name', 'subject', 'class_it_is_assigned_to', 'deadline_date', 'assignment_text', 'fines_information']
        labels = {'name': "Название",
                  'subject': "Предмет",
                  'class_it_is_assigned_to': "Класс",
                  'deadline_date': "Дедлайн",
                  'assignment_text': "Задание",
                  'fines_information': "Штраф"}

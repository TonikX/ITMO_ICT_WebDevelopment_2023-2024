from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RacerReg(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['experience', 'description', 'drive_class', 'team']


class CommentCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['main_text', 'type']

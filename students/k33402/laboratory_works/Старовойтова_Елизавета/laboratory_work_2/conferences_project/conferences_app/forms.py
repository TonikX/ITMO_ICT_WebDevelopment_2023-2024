from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']

class RegistrationForm(UserCreationForm):
    surname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    passport = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'surname', 'lastname', 'passport']

class LoginForm(AuthenticationForm):
    pass

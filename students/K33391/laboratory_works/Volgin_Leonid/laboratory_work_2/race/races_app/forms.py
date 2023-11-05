from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class RedactedUserCreationForm(UserCreationForm):
#     class Meta:
#         model = models.User
#         fields = ('firstname', 'lastname')


class RedactedAuthenticationForm(AuthenticationForm):
     class Meta:
         model = models.User
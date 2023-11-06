# forms.py в вашем приложении hotels
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Visitor

class VisitorCreationForm(UserCreationForm):
    class Meta:
        model = Visitor
        fields = ('username', 'email', 'phone_number',
                  'password1', 'password2')

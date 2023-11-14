from django import forms
from .models import Person, Treaty
from django.contrib.auth.forms import UserCreationForm


class CreatePersonForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [
            'username',
            'email',
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BookForm(forms.Form):
    startDate = forms.DateField(widget=forms.DateInput)
    pNum = forms.IntegerField()
    #endDate = forms.DateField(widget=forms.DateInput, disabled=True, )


class BookUpdForm(forms.ModelForm):
    class Meta:
        model = Treaty
        fields = ['startDate', 'pNum', 'cost']
    cost = forms.IntegerField()


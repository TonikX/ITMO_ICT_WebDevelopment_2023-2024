from django import forms
from django.contrib.auth.models import User
from .models import Racer, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_type", "rating", "text"]

class RacerForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ["full_name", "team", "biography", "num_of_races", "car_name"]

class RacerUpdateForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ["full_name", "team", "biography", "num_of_races", "car_name"]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"autocomplete": "off", "data-toggle": "password"})
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
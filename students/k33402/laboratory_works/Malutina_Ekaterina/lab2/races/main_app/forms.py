from django import forms
from .models import User, Register, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["type", "rating", "message"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email",
                  "description", "rating", "team", "car_num", "car_description"]

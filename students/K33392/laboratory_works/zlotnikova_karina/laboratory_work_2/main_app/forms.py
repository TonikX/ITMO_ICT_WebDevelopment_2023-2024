from django import forms
from .models import User, Register, Comment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email",
                  "description", "rating", "team", "car_num", "car_description"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["type", "rating", "message"]

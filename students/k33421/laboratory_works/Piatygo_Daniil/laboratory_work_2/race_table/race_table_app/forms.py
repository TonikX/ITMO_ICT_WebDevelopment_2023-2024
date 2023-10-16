from django import forms
from django.contrib.auth.models import User
from .models import Racer, Comment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]


class RacerForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ["team", "description", "experience"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_type", "rating", "text"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]


class RacerUpdateForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ["team", "description", "experience"]

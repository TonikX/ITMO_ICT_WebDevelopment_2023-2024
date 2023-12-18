from django import forms
from .models import Comment, UserProfile
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

    def save(self, commit=True):
        user = super().save(commit=False)

        user_profile = UserProfile(
            user=user,
            surname=self.cleaned_data['surname'],
            lastname=self.cleaned_data['lastname'],
            passport=self.cleaned_data['passport']
        )

        if commit:
            user.save()
            user_profile.save()

        return user

class LoginForm(AuthenticationForm):
    lastname = forms.CharField(max_length=100)
    passport = forms.CharField(max_length=20)

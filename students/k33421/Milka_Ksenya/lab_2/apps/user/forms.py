from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.user.models import Roles

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[(Roles.STUDENT, 'Student'), (Roles.TEACHER, 'Teacher')],
        required=True
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'date_of_birth', 'password1', 'password2', 'role')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from homeworks.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):
    pass

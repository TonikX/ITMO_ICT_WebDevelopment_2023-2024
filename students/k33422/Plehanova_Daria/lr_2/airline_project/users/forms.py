from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(label="Имя пользователя", max_length=150, required=True)
	password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)
	
	class Meta:
		model = get_user_model()
		fields = (
			'username', 'email', 'phone_number',
			'first_name', 'last_name', 'middle_name',
			'citizenship', 'date_of_birth', 'gender'
		)


class CustomAuthenticationForm(AuthenticationForm):
	username = forms.CharField(label="Имя пользователя")
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

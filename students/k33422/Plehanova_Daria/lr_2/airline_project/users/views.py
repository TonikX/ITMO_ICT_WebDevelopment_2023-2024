from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from . import forms


class UserRegisterView(CreateView):
	form_class = forms.CustomUserCreationForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')


class UserLoginView(LoginView):
	form_class = forms.CustomAuthenticationForm
	template_name = 'users/login.html'
	success_url = reverse_lazy('home')
	redirect_authenticated_user = True


class ForbiddenView(View):
	template_name = '403.html'
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, status=403)


class NotFoundView(View):
	template_name = '404.html'
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, status=404)

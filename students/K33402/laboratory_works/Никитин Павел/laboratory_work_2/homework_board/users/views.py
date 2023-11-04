from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from django.views import View


from users.forms import CustomUserCreationForm, CustomAuthenticationForm


def RegistrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form, "CHECK")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


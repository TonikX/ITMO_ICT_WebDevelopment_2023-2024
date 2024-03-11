from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *
from .models import *


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect("view_flights")

        messages.error(request, "Регистрация не удалась. Проверьте введённые данные.")
    else:
        form = RegistrationForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_func(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"Вы вошли как {user.username}.")
                return redirect("view_flights")
            else:
                messages.error(request, "Неверный логин или пароль.")
        else:
            messages.error(request, "Неверный логин или пароль.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_func(request):
    logout(request)
    messages.info(request, "Вы успешно вышли.")
    return redirect("login")


@login_required
def view_flights(request):
    flights = Flight.objects.exclude(reservations__user=request.user).filter(date__gt=timezone.now()).order_by("departure")
    return render(request, "flights_list.html", {"flights": flights})

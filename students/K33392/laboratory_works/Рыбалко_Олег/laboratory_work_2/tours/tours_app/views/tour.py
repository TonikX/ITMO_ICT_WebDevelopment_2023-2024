from os.path import join

from django.contrib.auth import authenticate, login
from django.forms import CharField, Form, ModelForm, PasswordInput
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from typing import Union

from tours_app.models import Tour

__BASE_TEMPLATE_PATH = "tour"

def all_tours_view(request: HttpRequest) -> HttpResponse:
    return render(request, join(__BASE_TEMPLATE_PATH, "all.html"), dict(tours=Tour.objects.all()))
    
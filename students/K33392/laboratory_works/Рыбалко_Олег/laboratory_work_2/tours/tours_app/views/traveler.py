from os.path import join

from django.contrib.auth import authenticate, login
from django.forms import CharField, Form, ModelForm, PasswordInput
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from typing import Union

from tours_app.models import Traveler

__BASE_TEMPLATE_PATH = "traveler"


class TravelerModelForm(ModelForm):
    class Meta:
        model = Traveler
        fields = ["first_name", "last_name", "username", "password"]


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


def create_traveler_view(request: HttpRequest) -> HttpResponse:
    if (form := TravelerModelForm(request.POST or None)).is_valid():
        form.save()
    return render(request, join(__BASE_TEMPLATE_PATH, "create.html"), dict(form=form))


def login_traveler_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)
    if request.method == "GET":
        return render(request, join(__BASE_TEMPLATE_PATH, "login.html"), dict(form=form))

    if not form.is_valid():
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))

    cd = form.cleaned_data
    try:
        user = Traveler.objects.get(username=cd["username"])
    except Traveler.DoesNotExist:
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))
    if user.password != cd["password"]:
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))

    login(request, user)
    return redirect(f"/profile/{user.pk}")


def traveler_profile_view(request: HttpRequest, pk: Union[int, None] = None) -> HttpResponse:
    user: Traveler = request.user
    if pk is None and (user is None or user.is_anonymous):
        return redirect("/login")
    return render(request, join(__BASE_TEMPLATE_PATH, "detail.html"), dict(user=user, tours=user.tours.all()))

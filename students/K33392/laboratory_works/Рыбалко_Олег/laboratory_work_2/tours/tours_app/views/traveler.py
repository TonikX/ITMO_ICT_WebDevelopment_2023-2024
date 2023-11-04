from os.path import join
from datetime import date
from typing import Union

from django.contrib.auth import login
from django.forms import CharField, Form, ModelForm, PasswordInput
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from tours_app.models import Reservation, Traveler

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
    if pk is None and user.is_anonymous:
        return redirect("/login")

    reservations = Reservation.objects.filter(traveler=user.pk)
    upcoming_reservations = list(filter(lambda x: x.tour_date.end_date > date.today(), reservations))
    archive_reservations = list(filter(lambda x: x.tour_date.end_date <= date.today(), reservations))
    return render(request, join(__BASE_TEMPLATE_PATH, "detail.html"), dict(user=user, upcoming_reservations=upcoming_reservations, archive_reservations=archive_reservations))

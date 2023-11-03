from os.path import join

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from project_first_app.models import Car

__BASE_PATH = "car"


def all_cars(request: HttpRequest) -> HttpResponse:
    return render(request, join(__BASE_PATH, "all.html"), dict(cars=Car.objects.all()))

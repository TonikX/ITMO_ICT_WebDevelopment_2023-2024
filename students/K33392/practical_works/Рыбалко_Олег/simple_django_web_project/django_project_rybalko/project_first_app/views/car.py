from os.path import join

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from project_first_app.models import Car

__BASE_PATH = "car"


def car(request: HttpRequest, car_id: int) -> HttpResponse:
    try:
        found_car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("car doesn't exist")

    return render(request, join(__BASE_PATH, "detail.html"), dict(car=found_car))


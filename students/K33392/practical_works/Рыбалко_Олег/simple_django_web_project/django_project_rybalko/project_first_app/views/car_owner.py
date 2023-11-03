from os.path import join

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from project_first_app.models import Car, CarOwner
from project_first_app.forms import CarOwnerModelForm

__BASE_PATH = "car_owner"


def car_owner(request: HttpRequest, owner_id: int) -> HttpResponse:
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("owner doesn't exist")

    return render(request, join(__BASE_PATH, "detail.html"), dict(owner=owner))


def all_owners(request: HttpRequest, car_id: int) -> HttpResponse:
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Car doesn't exist")
    return render(request, join(__BASE_PATH, "all.html"), dict(owners=car.owners.all()))


def create_car_owner(request: HttpRequest) -> HttpResponse:
    if (form := CarOwnerModelForm(request.POST or None)).is_valid():
        form.save()
    return render(request, join(__BASE_PATH, "create.html"), dict(form=form))

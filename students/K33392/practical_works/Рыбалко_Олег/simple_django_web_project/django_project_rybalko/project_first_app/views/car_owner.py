from os.path import join

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from project_first_app.models import CarOwner

__BASE_PATH = "car_owner"


def car_owner(request: HttpRequest, owner_id: str) -> HttpResponse:
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("owner doesn't exist")

    return render(request, join(__BASE_PATH, "detail.html"), dict(owner=owner))


def all_owners(request: HttpRequest) -> HttpResponse:
    return render(request, join(__BASE_PATH, "all.html"), dict(owners=CarOwner.objects.all()))

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .models import CarOwner


def car_owner(request: HttpRequest, owner_id: str) -> HttpResponse:
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("owner doesn't exist")

    return render(request, "car_owner/detail.html", dict(owner=owner))

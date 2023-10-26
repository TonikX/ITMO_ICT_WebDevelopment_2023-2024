from django.shortcuts import render
from django.http import Http404
from .models import CarOwner


def detail(req, id):
    try:
        owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("error")

    return render(req, "owner.html", {'owner': owner})



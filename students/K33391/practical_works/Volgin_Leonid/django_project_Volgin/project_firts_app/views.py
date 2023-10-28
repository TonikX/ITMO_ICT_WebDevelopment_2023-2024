from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import CarOwner


def get_car_owner(request, driver_id):
    try:
        car_owner = CarOwner.objects.get(pk=driver_id)
        #car_owner = CarOwner.objects.filter(surname="Valua")
        #print(car_owner)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "owner.html", {"car_owner": car_owner})
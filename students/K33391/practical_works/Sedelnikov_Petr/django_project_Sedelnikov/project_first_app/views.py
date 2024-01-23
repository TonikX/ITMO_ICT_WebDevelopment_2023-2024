from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .forms import *

def get_car_owner(request, driver_id):
    try:
        car_owner = CarOwner.objects.get(pk=driver_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "owner.html", {"car_owner": car_owner})

def get_car_owners_list(request):
    owners_list = CarOwner.objects.all()
    return render(request,"owners_list.html", {"owners_list": owners_list})

class CarDetailView(DetailView):
    model = Car
    template_name = "car.html"

class CarListView(ListView):
    model = Car
    template_name = "cars_list.html"

def create_car_owner(request):
    context = {}
    form = OwnerCreateForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)

class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = "create_car.html"
    success_url = "/cars_list"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = "update_car.html"
    success_url = "/cars_list"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "delete_car.html"
    success_url = "/cars_list"


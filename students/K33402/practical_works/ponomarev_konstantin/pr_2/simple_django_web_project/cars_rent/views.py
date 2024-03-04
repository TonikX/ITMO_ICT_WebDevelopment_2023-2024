from django.http import Http404
from django.shortcuts import render
from .models import Driver, Car
from .forms import DriverForm, CarForm
from django.views.generic.edit import DeleteView, UpdateView


def driver(request, id):
    try:
        driver = Driver.objects.get(id_driver=id)

    except Driver.DoesNotExist:
        raise Http404("Driver doesn't exist")
    return render(request, "driver.html", {"driver": driver})


def index(request):
    drivers = Driver.objects.all()
    cars = Car.objects.all()
    context = {
        "drivers": drivers,
        "cars": cars,
    }

    return render(request, "index.html", context)


def add_car(request):
    context = {}

    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "add_car.html", context)


def add_driver(request):
    context = {}

    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "add_driver.html", context)


def cars_list(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "car_list.html", context)


class DriverDeleteView(DeleteView):
    model = Driver
    template_name = "driver_confirm_delete.html"
    success_url = "/"


class DriverUpdateView(UpdateView):
    model = Driver
    template_name = "driver_update.html"
    fields = ["first_name", "last_name"]
    success_url = "/"

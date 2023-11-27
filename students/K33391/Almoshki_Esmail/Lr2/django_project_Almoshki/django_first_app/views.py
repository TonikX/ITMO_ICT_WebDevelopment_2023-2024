from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Driver, Car
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Arhiboooo")


def driver_page(request, id):
    driver = get_object_or_404(Driver, pk=id)
    return render(request, "django_first_app/driver.html", {"driver": driver})


def car_page(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "django_first_app/car.html", {"car": car})


class DriverListView(ListView):
    model = Driver
    template_name = "django_first_app/drivers.html"


class CarListView(ListView):
    model = Car
    template_name = "django_first_app/cars.html"


class DriverCreateView(CreateView):
    model = Driver
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = "../"


class CarCreateView(CreateView):
    model = Car
    fields = ['governmental_number', 'model', 'stamp', 'color']
    success_url = "../"


class CarDeleteView(DeleteView):
    model = Car
    success_url = "../../"
    template_name = "django_first_app/car_delete.html"


class CarUpdateView(UpdateView):
    model = Car
    success_url = reverse_lazy('car_list')
    fields = ['governmental_number', 'model', 'stamp', 'color']
    template_name = "django_first_app/car_update.html"

    def get_object(self):
        id_ = self.kwargs.get("")

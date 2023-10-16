from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import Driver, Car
from .forms import CarUpdateForm, DriverCreateForm, CarCreateForm


def index(request):
    return render(request, "project_first_app/index.html")


def get_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, "project_first_app/get_driver.html", {"driver": driver})


def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, "project_first_app/list_drivers.html", {"drivers": drivers})


def create_driver(request):
    match request.method:
        case "POST":
            form = DriverCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("list_drivers")
        case "GET":
            form = DriverCreateForm()
            return render(
                request, "project_first_app/create_driver_view.html", {"form": form}
            )
        case _:
            return Http404(f"Method {request.method} not supported")


class CarDetailView(DetailView):
    model = Car
    template_name = "project_first_app/car_detail_view.html"
    context_object_name = "car"


class CarListView(ListView):
    model = Car
    template_name = "project_first_app/cars_list_view.html"
    context_object_name = "cars"


class CarCreateView(CreateView):
    model = Car
    template_name = "project_first_app/car_create_view.html"
    form_class = CarCreateForm
    success_url = "/cars"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    success_url = "/cars"
    template_name = "project_first_app/car_update_view.html"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "project_first_app/car_delete_view.html"
    success_url = "/cars"

from django.shortcuts import render
from .models import Driver, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import Http404
from .forms import DriverForm


def detail(request, id):
    try:
        driver = Driver.objects.get(pk=id)

    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, 'car_rent/driverDetails.html', {'driver': driver, 'id': id})


def index(request):
    return render(request, 'car_rent/index.html')


def cars(request):
    cars_data = Car.objects.all()
    return render(request, 'car_rent/cars.html', {"cars": cars_data})


class DriverList(ListView):
    model = Driver
    template_name = 'car_rent/drivers.html'


class CarView(DetailView):
    model = Car


class CarCreate(CreateView):
    model = Car
    template_name = 'car_rent/cvb_create_view.html'

    # specify the fields to be displayed

    fields = ['number', 'brand', 'car_model', 'color']


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'car_model', 'color']
    success_url = '/cars'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'


class DriverUpdateView(UpdateView):
    model = Driver
    fields = ["first_name", "last_name", "birth_date"]
    success_url = '/drivers'


def create_view(request):
    context = {}
    form = DriverForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "car_rent/create_view.html", context)


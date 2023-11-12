from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Driver, Car
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DriverForm, CarForm


def homepage(request):
    return render(request, 'homepage.html', {})


def all_drivers(request):
    d_list = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': d_list})


def get_driver(request, driver_id):
    d = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'driver.html', {'d': d})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-drivers')
    else:
        form = DriverForm()
    return render(request, 'create_driver.html', {'form': form})


class CarView(ListView):
    model = Car
    template_name = 'cars.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'create_car.html'
    form_class = CarForm
    success_url = reverse_lazy('all-cars')


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'update_car.html'
    form_class = CarForm
    success_url = reverse_lazy('all-cars')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = reverse_lazy('all-cars')
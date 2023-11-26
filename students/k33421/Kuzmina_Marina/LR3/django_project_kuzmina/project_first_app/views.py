from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Driver, Car
from .forms import *


def index(request):
    return render(request, 'index.html')


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'create_driver.html', {'form': form})


def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'update_driver.html', {'form': form, 'driver': driver})


def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'delete_driver.html', {'driver': driver})


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    model = Car
    template_name = 'create_car.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('car_list')


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'update_car.html'
    form_class = CarUpdateForm
    success_url = reverse_lazy('car_list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = reverse_lazy('car_list')
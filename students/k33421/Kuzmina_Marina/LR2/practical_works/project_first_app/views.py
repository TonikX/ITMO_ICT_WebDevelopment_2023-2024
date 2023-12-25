from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Driver, Car
from .forms import *


def index(request):
    return render(request, 'project_first_app/index.html')


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'project_first_app/driver_list.html', {'drivers': drivers})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'project_first_app/driver_creation.html', {'form': form})


def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'project_first_app/driver_update.html', {'form': form, 'driver': driver})


def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'project_first_app/driver_deletion.html', {'driver': driver})


class CarListView(ListView):
    model = Car
    template_name = 'project_first_app/car_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'project_first_app/car_detail.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    model = Car
    template_name = 'project_first_app/car_creation.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('car_list')


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'project_first_app/car_update.html'
    form_class = CarUpdateForm
    success_url = reverse_lazy('car_list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'project_first_app/car_deletion.html'
    success_url = reverse_lazy('car_list')

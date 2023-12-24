from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Driver, Auto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DriverForm, AutoForm


def home(request):
    return render(request, 'home.html', {})


def all_drivers(request):
    d_list = Driver.objects.all()
    return render(request, 'owners.html', {'drivers': d_list})


def get_driver(request, driver_id):
    d = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'owner.html', {'d': d})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-drivers')
    else:
        form = DriverForm()
    return render(request, 'create_driver.html', {'form': form})


class AutoView(ListView):
    model = Auto
    template_name = 'autos.html'


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'auto.html'


class AutoCreateView(CreateView):
    model = Auto
    template_name = 'create_auto.html'
    form_class = AutoForm
    success_url = reverse_lazy('all-autos')


class AutoUpdateView(UpdateView):
    model = Auto
    template_name = 'update_auto.html'
    form_class = AutoForm
    success_url = reverse_lazy('all-autos')


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'delete_auto.html'
    success_url = reverse_lazy('all-autos')
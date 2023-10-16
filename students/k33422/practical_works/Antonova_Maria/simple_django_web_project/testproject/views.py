from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse

from .models import Car_owner, Car, Ownership, Driver_license
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import CreateOwner


def info_about_car_owner(request, id_owner):
    try:
        owner = Car_owner.objects.get(pk=id_owner)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def all_owners(request):
    return render(request, 'list_owners.html', {'all_owners': Car_owner.objects.all()})


class CarList(ListView):
    model = Car
    template_name = 'list_cars.html'


class CarById(DetailView):
    model = Car
    template_name = 'car.html'


def create_owner(request):
    context = {}
    form = CreateOwner(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('list_owners'))
    context['form'] = form
    return render(request, 'create_owner.html', context)


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'mark_car', 'model_car', 'color']
    template_name = 'update_car.html'
    success_url = '/list_cars/'


class CarCreate(CreateView):
    model = Car
    fields = ['state_number', 'mark_car', 'model_car', 'color']
    template_name = 'create_car.html'
    success_url = '/list_cars/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_cars.html'
    success_url = '/list_cars/'

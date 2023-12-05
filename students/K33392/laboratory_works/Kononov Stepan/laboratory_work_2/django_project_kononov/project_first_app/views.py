from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import CarOwnerForm, CarForm
from .models import Car
from .models import CarOwner


def owner_detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def all_owners(request):
    owners = CarOwner.objects.all()
    return render(request, 'all_owners.html', {'owners': owners})


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


def add_car_owner(request):
    if request.method == 'POST':
        form = CarOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_owners')
    else:
        form = CarOwnerForm()

    return render(request, 'add_car_owner.html', {'form': form})


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create_car.html'
    success_url = '/cars'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update_car.html'
    success_url = '/cars'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars'

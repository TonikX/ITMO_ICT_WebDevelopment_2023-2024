from django.shortcuts import render
from .models import Owner, Car
from .forms import OwnerForm, CarForm
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class OwnerRetrieveView(DetailView):
    template_name = 'owner/ownerDetail.html'
    queryset = Owner.objects.all()

def index(request):
    owners = Owner.objects.all()
    cars = Car.objects.all()
    context = {
        'owners': owners,
        'cars': cars,
    }

    return render(request, 'index.html', context)

def addCar(request):
    context = {}

    form = CarForm(request.POST or None)
    if (form.is_valid()):
        form.save()
    context['form'] = form
    return render(request, 'addCar.html', context)
def addOwner(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if (form.is_valid()):
        form.save()
    context['form'] = form
    return render(request, 'addOwner.html', context)

def car_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'car_list.html', context)

class OwnerDelete(DeleteView):
    model = Owner
    template_name = "owner_confirm_delete.html"
    success_url = '/'

class OwnerUpdateView(UpdateView):
    model = Owner
    template_name = 'owner_update.html'
    fields = ['first_name', 'last_name']
    success_url = '/'

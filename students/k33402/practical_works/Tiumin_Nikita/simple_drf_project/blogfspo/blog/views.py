from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from django.http import Http404
from django.shortcuts import render
from .models import Owner, Car

from .forms import CreateOwnerForm


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
        print(owner.cars)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.show.html', {'owner': owner})


def index_owners(request):
    owners = Owner.objects.all()
    return render(request, 'owner.index.html', {'owners': owners})


class CarList(ListView):
    model = Car
    template_name = 'car.index.html'


class CarDetails(DetailView):
    model = Car
    template_name = 'car.show.html'

#--------------------------forms


def create_owner(request):
    context = {}

    form = CreateOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, "owner.create.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = [
        'license_plate',
        'brand',
        'model',
        'color'
    ]
    success_url = '/cars'
    template_name = 'car.update.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car.create.html'
    success_url = '/cars'
    fields = [
        'license_plate',
        'brand',
        'model',
        'color'
    ]


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'
    template_name = 'car.delete.html'

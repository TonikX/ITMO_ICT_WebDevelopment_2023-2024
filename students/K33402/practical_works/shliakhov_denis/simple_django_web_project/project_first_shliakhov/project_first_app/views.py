from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .forms import OwnerForm
from .models import Owner, Car


def owners(request):
    visual = {"owners": Owner.objects.all()}
    return render(request, 'owners.html', visual)


def owner(request, pk):
    try:
        founded_owner = Owner.objects.get(pk=pk)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': founded_owner})


def create_owner_view(request):
    visual = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    visual['form'] = form
    return render(request, 'create_owner.html', visual)


def cars(request):
    visual = {"cars": Car.objects.all()}
    return render(request, 'cars.html', visual)


class CarView(DetailView):
    model = Car
    template_name = 'car.html'


class CreateCar(CreateView):
    model = Car
    template_name = 'create_car.html'
    fields = ['id', 'state_number', 'brand', 'model', 'color']
    success_url = '/cars/'


class UpdateCarView(UpdateView):
    model = Car
    fields = ['id', 'state_number', 'brand', 'model', 'color']
    success_url = '/cars/'
    template_name = 'update_car.html'


class DeleteCarView(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'delete_car.html'

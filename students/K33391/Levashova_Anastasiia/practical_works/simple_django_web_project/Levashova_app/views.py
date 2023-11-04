from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CarOwnerForm, CarCreateForm, CarUpdateForm
from .models import CarOwner, Car
from django.views.generic.list import ListView


def car_owner_detail(request, car_owner_id):
    try:
        owner = CarOwner.objects.get(pk=car_owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'CarOwner.html', {'owner': owner})


def car_owners_list_view(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "CarOwnersList.html", context)


class CarsList(ListView):
    model = Car
    template_name = 'CarsList.html'


def car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'Car.html', {'car': car})


def create_owner(request):
    context = {}
    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "OwnerForm.html", context)


class CreateCar(CreateView):
    model = Car
    form_class = CarCreateForm
    success_url = '/cars'
    template_name = "CarCreateForm.html"


class UpdateCar(UpdateView):
    model = Car
    form_class = CarUpdateForm
    success_url = "/cars"
    template_name = "CarUpdateForm.html"


class DeleteCar(DeleteView):
    model = Car
    template_name = "CarDelete.html"
    success_url = "/cars"

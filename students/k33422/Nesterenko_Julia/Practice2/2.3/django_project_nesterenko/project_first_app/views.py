from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Car
from .forms import OwnerForm


def owner(request, id):
    try:
        o = get_user_model().objects.get(pk=id)
    except get_user_model().DoesNotExist:
        raise Http404("Not found")
    return render(request, 'owner.html', {'owner': o})


def owner_list(request):
    try:
        o_list = get_user_model().objects.all()
    except get_user_model().DoesNotExist:
        raise Http404("Not found")
    context = {'owners': o_list}
    return render(request, 'owner_list.html', context)


def create_owner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'create_owner.html', context)


class CarRetrieveView(DetailView):
    model = Car


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarCreateView(CreateView):
    model = Car
    fields = ['license_plate',
              'brand',
              'model',
              'color']
    template_name = 'car_create.html'
    success_url = '/car/list/'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['license_plate',
              'brand',
              'model',
              'color']
    template_name = 'car_update.html'
    success_url = '/car/list/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car/list/'

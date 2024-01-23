from django.shortcuts import render
from django.http import Http404
from .models import Owner, Car, Possession
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def get_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'show_owner.html', {'owner': owner})


def get_car_owners(request, car_id):
    try:
        # car = Car.objects.get(pk=car_id)
        owner = None
        for item in (Possession.objects.filter(car_id=car_id)):
            if item.end_date is None:
                owner = item.owner_id
                break
        if owner is None:
            return render(request, 'show_none_owner.html')
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

    return render(request, 'show_owners.html', {'owners': owner})


def get_owners(request):
    owners = dict()
    owners["dataset"] = Owner.objects.all()

    return render(request, "show_owners_list.html", owners)


def owner_form_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)


class CarList(ListView):
    model = Car
    template_name = 'show_all_cars.html'


class CarById(DetailView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    fields = ['owner', 'license_plate', 'color']
    success_url = '../car/list'


class CarCreateView(CreateView):
    model = Car
    template_name = 'create_car_form.html'
    fields = ['owner', 'license_plate', 'brand', 'model', 'color']
    success_url = '/car/list'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '../car/list'

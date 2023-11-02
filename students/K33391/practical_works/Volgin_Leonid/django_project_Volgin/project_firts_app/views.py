from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import CarOwnerCreateForm, CarCreateForm, CarUpdateForm
from .models import CarOwner, Car
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

def get_car_owner(request, driver_id):
    try:
        car_owner = CarOwner.objects.get(pk=driver_id)
        #car_owner = CarOwner.objects.filter(surname="Valua")
        #print(car_owner.cars.all())
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "owner.html", {"car_owner": car_owner})

def get_car_owners_list(request):
    car_owners_list = CarOwner.objects.all()
    return render(request,"list_of_car_owners.html", {"car_owners_list": car_owners_list})

class CarDetailView(DetailView):
    model = Car
    template_name = "project_first_app/car_detail_view.html"
    context_object_name = "car"


class CarListView(ListView):
    model = Car
    template_name = "list_of_cars.html"

class CarDetailView(DetailView):
    model = Car
    template_name = "car.html"

class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    template_name = 'update_car.html'
    success_url = '/list_of_cars'


def create_car_owner(request):
    context = {}
    form = CarOwnerCreateForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_car_owner.html", context)


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = "create_car.html"
    success_url = "/list_of_cars"


class CarUpdateViewWithForm(UpdateView):
    model = Car
    form_class = CarUpdateForm
    template_name = "update_car_with_form.html"
    success_url = "/list_of_cars"






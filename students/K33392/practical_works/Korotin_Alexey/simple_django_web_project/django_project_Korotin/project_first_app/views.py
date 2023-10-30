from django.shortcuts import render
from django.http import Http404
from .models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView


def detail(req, id):
    try:
        owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("error")

    return render(req, "owner.html", {'owner': owner})


def get_all_owners(req):
    owners = CarOwner.objects.all()

    return render(req, "owner_list.html", {"owners": owners})


class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()
    template_name = "car_list.html"

    def get_queryset(self):
        car_id = self.request.GET.get('id')

        if car_id:

            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(id=car_id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class UpdateCardView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'license_plate']
    success_url = '/cars'
    template_name = "car_form.html"


class CreateUserView(CreateView):
    model = CarOwner
    fields = ['first_name', 'last_name', 'passport', 'nationality', 'birth_date', 'home_Address']
    success_url = "/owners"
    template_name = "user_form.html"

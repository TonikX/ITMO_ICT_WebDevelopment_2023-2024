from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Driver, Car
from .forms import DriverForm


def detail(request, id):
    try:
        d = Driver.objects.get(pk=id)

    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, 'project_first_app/owner.html', {'owner': d})


def driver_list(request):
    context = {"dataset": Driver.objects.all()}

    return render(request, "project_first_app/driver_list.html", context)


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = DriverForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "project_first_app/create_view.html", context)


class CarList(ListView):
    model = Car
    template_name = 'project_first_app/car_list.html'


class CarView(DetailView):
    model = Car


class DriverUpdateView(UpdateView):
    model = Driver
    fields = ["first_name", "last_name", "birth_date"]
    success_url = '/drivers'


class CarCreate(CreateView):
    # specify the model for create view
    model = Car
    template_name = 'project_first_app/cvb_create_view.html'

    # specify the fields to be displayed

    fields = ['number', 'brand', 'car_model', 'color']


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'car_model', 'color']
    success_url = '/cars'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'

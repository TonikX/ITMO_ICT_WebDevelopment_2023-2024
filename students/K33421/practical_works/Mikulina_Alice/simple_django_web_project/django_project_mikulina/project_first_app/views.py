from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import Http404, HttpResponse
from .forms import *
from .models import *
import datetime


def show_driver(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)  
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, 'driver.html', {'driver': driver})


def show_time(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


def list_drivers(request):
    context ={}

    context["drivers"] = Driver.objects.all()
    print(context)
          
    return render(request, "list_drivers.html", context)


def create_driver(request):
    context ={}
  
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "success.html")
    context['form'] = form
    return render(request, "create_driver.html", context)


class CarList(ListView):
    model = Car
    template_name = 'list_cars.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car.html'


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = 'car_list_by_drivers.html'

    def get_queryset(self):
        self.queryset = self.model.objects.all()
        drivers = self.request.GET.get('drivers')
        
        if drivers:

            try:
                drivers = int(drivers)
                queryset = self.queryset.filter(drivers=drivers)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'colour']
    template_name = 'car_update.html'
    success_url = '/car/list/'


class CarCreate(CreateView):
   model = Car
   template_name = 'car_create.html'

   fields = ['number', 'brand', 'model', 'colour']
   success_url = '/car/list/'


class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_delete.html'
  success_url = '/publisher/list/'

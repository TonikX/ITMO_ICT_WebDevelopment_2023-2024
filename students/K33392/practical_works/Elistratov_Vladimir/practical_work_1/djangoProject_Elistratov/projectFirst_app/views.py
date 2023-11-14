import datetime

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import CarOwner
from .models import Car

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from .forms import CarOwnerForm

# Create your views here.


def CarOwnersList(request):
    people = {}
    try:
        people["dataset"] = CarOwner.objects.all()
    except CarOwner.DoesNotExist:
        raise Http404("SWW")

    return render(request, 'ownerList.html', people)


def CarOwnersDetail(request, carOwnerId):
    try:
        people = CarOwner.objects.get(pk=carOwnerId)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")

    return render(request, 'ownerOne.html', {'owner': people})


class CarListView(ListView):
    model = Car
    template_name = 'carList.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'carDetail.html'


def CreateCarOwner(request):
    context = {}
    form = CarOwnerForm(request.POST or None)
    if(form.is_valid()):
        form.save()
    context['form'] = form
    return render(request, "NewCarOwner.html", context)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'carEdit.html'
    fields = ['govNumber', 'brand', 'model', 'color']
    success_url = '/car/'


class CarCreateView(CreateView):
    model = Car
    template_name = 'carEdit.html'
    fields = ['govNumber', 'brand', 'model', 'color']
    success_url = '/car/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'carDelete.html'
    success_url = '/car/'

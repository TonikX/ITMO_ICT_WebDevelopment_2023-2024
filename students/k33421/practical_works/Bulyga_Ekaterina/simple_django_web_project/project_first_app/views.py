from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import CarOwner, Car
from django.views.generic.list import ListView
from .forms import CarOwnerForm
from django.views.generic.edit import CreateView


def detail(request):
    owners = CarOwner.objects.all()
    return render(request, 'owner.html', {'owners': owners})


# TODO: не происходит обновление данных
class AutoList(ListView):
    model = Car
    template_name = 'car.html'
    queryset = model.objects.all()

    def get_queryset(self):
        id = self.request.GET.get('id')

        if id:

            try:
                id = int(id)
                print(id)
                queryset = self.queryset.filter(id=id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def ownerForm(request):
    context = {}

    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "form.html", context)


class CarCreateForm(CreateView):
   model = Car
   template_name = 'create.html'

   fields = ['number', 'brand', 'model', 'color']


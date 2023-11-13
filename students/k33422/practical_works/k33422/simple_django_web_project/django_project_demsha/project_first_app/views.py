from django.http import Http404
from django.shortcuts import render
from project_first_app.models import User, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def owner_detail(request, owner_id):
    try:
        p = User.objects.get(pk=owner_id)
        print(p.last_name)
    except User.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'single_owner.html', {'owner': p})


def owners_list_view(request):
    context = {}
    context["dataset"] = User.objects.all()

    return render(request, "owners_list.html", context)


def create_owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner_view.html", context)


# class CarListView(ListView):
#     model = Car
#     template_name = 'cars_list_view.html'


class CarListView(ListView):
    model = Car

class CarRetrieveView(DetailView):
  model = Car


class CarUpdateView(UpdateView):
  model = Car
  fields = ['brand', 'model','color']
  success_url = '/car/list/'


class CarCreate(CreateView):
  model = Car
  fields = ['license_plate_number', 'brand', 'model','color']
  template_name = 'car_create_view.html'


class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car/list/'

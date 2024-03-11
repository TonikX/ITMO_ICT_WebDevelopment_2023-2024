from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import CustomUserCreationForm
from .models import CarOwner, Car


def owner_details(request, owner_id):
    try:
        car_owner = CarOwner.objects.get(
            pk=owner_id)

    except CarOwner.DoesNotExist:
        raise Http404(
            "Poll does not exist")

    return render(request, '../templates/owner.html', {'owner': car_owner})


def list_owners_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["owners"] = CarOwner.objects.all()

    return render(request, "list_owners_view.html", context)


class CarListView(ListView):
    model = Car
    template_name = 'list_cars_view.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


# relative import of forms
from .forms import CarOwnerForm  # импортируем только-что созданную форму


def create_owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CarOwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner_form.html", context)


from django.views.generic.edit import UpdateView, CreateView, DeleteView


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['gov_num', 'car_mark', 'car_model', 'color']
    success_url = '/cars_list/'


class CarCreateView(CreateView):
    # specify the model for create view
    model = Car
    template_name = 'car_create.html'
    success_url = '/cars_list/'

    fields = ['gov_num', 'car_mark', 'car_model', 'color']


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars_list/'


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin/")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

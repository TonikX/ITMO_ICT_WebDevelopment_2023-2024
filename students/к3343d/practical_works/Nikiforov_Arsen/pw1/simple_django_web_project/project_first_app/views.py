from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Owner, Car, Ownership, DriverLicense, ExampleModel
from .forms import ExampleForm
from django.shortcuts import render, redirect
from .forms import OwnerForm
from .forms import CarForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy 




class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'



class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create_car.html'
    success_url = '/car/list/'  # URL для перенаправления после успешного создания


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update_car.html'
    success_url = '/car/list/'  # URL для перенаправления после успешного обновления




class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/car/list/'  # URL для перенаправления после успешного удаления



def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()
    
    return render(request, 'create_car.html', {'form': form})



def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_owners')  # Перенаправление на список владельцев
    else:
        form = OwnerForm()
    return render(request, 'create_owner.html', {'form': form})






def create_view(request):
    context = {}
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)













# Список машин
def car_list(request):
    make = request.GET.get('make')
    model = request.GET.get('model')
    car_id = request.GET.get('car_id')

    queryset = Car.objects.all()

    if make:
        queryset = queryset.filter(make__icontains=make)

    if model:
        queryset = queryset.filter(model__icontains=model)

    if car_id:
        queryset = queryset.filter(pk=car_id)

    cars = queryset

    return render(request, 'car_list.html', {'cars': cars})

# Не важно, это я для себя добавил, чтобы посмотреть список людей и фильтровать
class OwnerListView(ListView):
    model = Owner
    template_name = 'owner_list.html'

    def get_queryset(self):
        last_name = self.request.GET.get('last_name')
        first_name = self.request.GET.get('first_name')

        queryset = Owner.objects.all()

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        
        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_name'] = self.request.GET.get('last_name', '')
        context['first_name'] = self.request.GET.get('first_name', '')
        return context

class ExampleList(ListView):
    model = Owner
    template_name = 'cvb_list_view.html'

def owner_list(request):
    last_name = request.GET.get('last_name')
    first_name = request.GET.get('first_name')
    owners = Owner.objects.all()

    if last_name:
        owners = owners.filter(last_name__icontains=last_name)

    if first_name:
        owners = owners.filter(first_name__icontains=first_name)

    return render(request, 'project_first_app/owner_list.html', {'owners': owners})

def list_view(request):
    context = {}
    context["dataset"] = ExampleModel.objects.all()
    return render(request, "list_view.html", context)

def owner_detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Владелец не найден.")
    return render(request, 'owner.html', {'owner': owner})

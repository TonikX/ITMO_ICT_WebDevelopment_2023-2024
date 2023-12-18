from django.shortcuts import render, redirect
from .models import Owner, Car
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from .forms import OwnerForm, CarForm, CarDeleteByIdForm, UserProfileForm

def add_owner(request):
    if request.method == 'POST':
        owner_form = OwnerForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        if owner_form.is_valid() and user_profile_form.is_valid():
            owner = owner_form.save(commit=False)
            owner.user_profile = user_profile_form.save()
            owner.save()
            return redirect('owner_list')
    else:
        owner_form = OwnerForm()
        user_profile_form = UserProfileForm()

    return render(request, 'add_owner.html', {'owner_form': owner_form, 'user_profile_form': user_profile_form})

def owner_detail(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    user_profile = owner.user_profile  # Получаем профиль пользователя

    return render(request, 'owner_detail.html', {'owner': owner, 'user_profile': user_profile})
def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = '/cars/'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    success_url = '/cars/'


class CarDeleteByIdView(View):
    template_name = 'car_delete_by_id.html'

    def get(self, request, car_id):
        form = CarDeleteByIdForm(initial={'car_id': car_id})
        return render(request, self.template_name, {'form': form})

    def post(self, request, car_id):
        form = CarDeleteByIdForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data.get('car_id')
            try:
                car = Car.objects.get(pk=car_id)
                car.delete()
                return redirect('car_list')  # Перенаправить пользователя на страницу со списком автомобилей
            except Car.DoesNotExist:
                form.add_error('car_id', 'Автомобиль с указанным ID не найден.')
        return render(request, self.template_name, {'form': form})
def index(request):
    return render(request, 'index.html')

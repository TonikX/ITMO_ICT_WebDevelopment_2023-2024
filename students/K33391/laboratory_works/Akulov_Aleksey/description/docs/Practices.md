# Отчет по практикам

Выполнил: Акулов Алексей, K33391

## Практика по 2 лабораторной

### Model

В итоге после выполнения всех трех практик получается вот такая модель

```
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class CarOwner(AbstractUser):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True, blank=True)
    passport = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)
    cars = models.ManyToManyField("Car", through="Ownership")


class DrivingLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)
    owners = models.ManyToManyField("CarOwner", through="Ownership")


class Ownership(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

```

### Views

```

from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404
#импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, DetailView, \
    UpdateView

from .forms import CarUpdateForm, OwnerCreateForm, CarCreateForm
from .models import CarOwner, Car


def index(request):
    return render(request, "index.html")

def detail(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=owner_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'owner.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"

def owner_get(request, owner_id):
    owner = get_object_or_404(CarOwner, pk=owner_id)
    return render(request, "owner_get.html", {"owner": owner})


def owner_list(request):
    owners = CarOwner.objects.all()
    return render(request, "owner_list.html", {"owners": owners})

def owner_create(request):
    match request.method:
        case "POST":
            form = OwnerCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("owner_list")
        case "GET":
            form = OwnerCreateForm()
            return render(
                request, "owner_create.html", {"form": form}
            )
        case _:
            return Http404(f"Method {request.method} not supported")


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail_view.html"
    context_object_name = "car"


class CarListView(ListView):
    model = Car
    template_name = "car_list_view.html"
    context_object_name = "cars"


class CarCreateView(CreateView):
    model = Car
    template_name = "car_create_view.html"
    form_class = CarCreateForm
    success_url = "/cars"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarUpdateForm
    success_url = "/cars"
    template_name = "car_update_view.html"

class CarDeleteView(DeleteView):
    model = Car
    success_url = "/cars"
    template_name = "car_delete_view.html"
```

## Практика по 3 лабораторной

### Практическое задание 2

```
from django.shortcuts import render
from .models import Car, CarOwner, DrivingLicense, Ownership
from django.db import models
from django.utils import timezone

def cars_by_brand(request, brand="Toyota"):
    cars = Car.objects.filter(brand=brand)
    return render(request, 'cars_by_brand.html', {'cars': cars})

def drivers_by_name(request, name="Олег"):
    drivers = CarOwner.objects.filter(name=name)
    return render(request, 'drivers_by_name.html', {'drivers': drivers})

def license_by_owner_id(request):
    random_owner = CarOwner.objects.order_by('?').first()
    if random_owner:
        owner_id = random_owner.id
        license = DrivingLicense.objects.filter(owner_id=owner_id).first()
    else:
        license = None
    return render(request, 'license_by_owner_id.html', {'license': license})

def owners_of_red_cars(request, color="красный"):
    owners = CarOwner.objects.filter(cars__color=color).distinct()
    return render(request, 'owners_of_red_cars.html', {'owners': owners})

def owners_starting_from_year(request, year=2010):
    owners = Ownership.objects.filter(start_date__year=year).select_related('owner').distinct()
    return render(request, 'owners_starting_from_year.html', {'owners': owners})

```

### Практическое задание 3

```
from django.shortcuts import render
from .models import CarOwner, DrivingLicense, Ownership, Car
from django.db import models

def oldest_license(request):
    oldest_license = DrivingLicense.objects.earliest('issue_date')
    return render(request, 'oldest_license.html', {'oldest_license': oldest_license})

def latest_ownership(request):
    latest_ownership_date = Ownership.objects.filter(car__model__isnull=False).latest('end_date').end_date
    return render(request, 'latest_ownership.html', {'latest_ownership_date': latest_ownership_date})

def car_count_per_owner(request):
    owners_with_car_count = CarOwner.objects.annotate(car_count=models.Count('cars'))
    return render(request, 'car_count_per_owner.html', {'owners_with_car_count': owners_with_car_count})

def car_count_by_brand(request):
    car_count = Car.objects.values('brand').annotate(count=models.Count('id'))
    return render(request, 'car_count_by_brand.html', {'car_count': car_count})

def owners_sorted_by_license_issue_date(request):
    owners_sorted = CarOwner.objects.annotate(earliest_license_issue_date=models.Min('drivinglicense__issue_date')).order_by('earliest_license_issue_date').distinct()
    return render(request, 'owners_sorted_by_license.html', {'owners_sorted': owners_sorted})

```
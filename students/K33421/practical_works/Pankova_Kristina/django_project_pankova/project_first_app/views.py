from django.shortcuts import render

from django.http import Http404
#импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from .models import * #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.http import HttpResponse
import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .forms import CarOwnerForm  # импортируем только-что созданную форму

from django.views.generic.edit import DeleteView

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/cars/list/'
  template_name = 'delete_car.html'


class CarCreateView(CreateView):
  model = Car
  fields = ['gov_number', 'car_make', 'model', 'color']
  template_name = 'car_create_view.html'

class CarUpdateView(UpdateView):
  model = Car
  fields = ['gov_number', 'car_make', 'model', 'color']
  success_url = '/cars/list/'
  template_name = 'update_car.html'


def create_car_owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CarOwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_carowner.html", context)


class CarList(ListView):
    model = Car
    template_name = 'list_cars.html'

class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


# views.py
class CarsOfOwnerListView(ListView):
    template_name = 'list_cars_by_owner.html'
    model = Car
    def get_queryset(self):
        self.queryset = self.model.objects.all()

        car_owner = self.request.GET.get('owner')

        if car_owner:
            try:
                print(self.queryset[0].owner)
                car_owner = int(car_owner)
                queryset = self.queryset.filter(owner=car_owner)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset

def owner_detail(request, carowner_id):
    try:
        p = CarOwner.objects.get(pk=carowner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'carowners.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"


def list_carowners_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = CarOwner.objects.all()
    print(context["dataset"])

    return render(request, "list_carowners.html", context)


def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


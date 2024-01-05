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



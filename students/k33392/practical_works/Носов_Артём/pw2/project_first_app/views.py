from django.http import Http404 
#импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from project_first_app.models import Book, Owner, ExampleModel, Publisher #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.views.generic.list import ListView

from project_first_app.forms import ExampleForm

def detail(request, id):
    try: #метод try-except - обработчик исключений
        p = Owner.objects.get(pk=id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'owner.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"

# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
  
# create a function
def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь 
    context["dataset"] = ExampleModel.objects.all()
          
    return render(request, "list_view.html", context)

class ExampleList(ListView):
  
    # specify the model for list view
    model = ExampleModel
    template_name = 'cvb_list_view.html'

from django.views.generic.detail import DetailView

class PublisherRetrieveView(DetailView):
  model = Publisher

class BookListView(ListView):
  model = Book
  queryset = model.objects.all()

  def get_queryset(self):
    publisher = self.request.GET.get('publisher')
    
    if publisher:
        try:
            publisher = int(publisher)
            queryset = self.queryset.filter(publisher=publisher)
        except ValueError:
            queryset = self.model.objects.none()

        return queryset

    return self.queryset
  
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = ExampleForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

from django.views.generic.edit import UpdateView, CreateView
class PublisherUpdateView(UpdateView):
  model = Publisher
  fields = ['first_name', 'last_name', 'birthdate']
  success_url = '/publisher/list/'


class ExampleCreate(CreateView):

   # specify the model for create view
   model = ExampleModel
   template_name = 'cvb_create_view.html'

   # specify the fields to be displayed

   fields = ['title', 'description']

class PublisherUpdateView(CreateView):
  model = Publisher
  fields = ['first_name', 'last_name', 'birthdate']
  success_url = '/publisher/list/'

from django.views.generic.edit import DeleteView

class PublisherDeleteView(DeleteView):
  model = Publisher
  success_url = '/publisher/list/'


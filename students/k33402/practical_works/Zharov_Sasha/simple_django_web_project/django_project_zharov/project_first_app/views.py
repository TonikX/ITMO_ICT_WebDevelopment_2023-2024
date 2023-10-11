from django.http import Http404
from django.shortcuts import render
from .models import Driver


def detail(request, id):
    try:
        d = Driver.objects.get(pk=id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
        #d = Driver.objects.all()
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'project_first_app/owner.html', {'owner': d}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"

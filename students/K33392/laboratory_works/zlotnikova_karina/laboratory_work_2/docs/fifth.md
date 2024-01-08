# Таблица заездов.

### В клиентской части должна формироваться таблица всех заездов и результатов конкретной гонки.

###### Модель гонки/заезда

```
class Race(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name ='Гонка'
        verbose_name_plural='Гонки'

```
###### Метод вывода списка заездов
```
def races_list(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    races = Race.objects.all()

    return render(
        request,
        "races_list.html",
        {"races": races},
    )
```
###### Страница таблицы заездов
```
{% extends 'base.html' %} {% block content %}

<h1 class="text-center">Races schedule</h1>

<table class="table table-striped table-hover mb-5">
  <thead>
    <tr>
      <th scope="col">Name:</th>
      <th scope="col">When:</th>
      <th scope="col">Ended:</th>
      <th scope="col">Details:</th>
    </tr>
  </thead>

  <tbody>
    {% for race in races %}
      <tr>
        <td>{{race.name}}</td>
        <td>{{race.when}}</td>
        <td>{{race.finished}}</td>
        <td><a href="{% url 'race_detail' race.id %}">Details</a></td>
      </tr>
    {% endfor %}
  </tbody>
</table>

{% endblock %}
```
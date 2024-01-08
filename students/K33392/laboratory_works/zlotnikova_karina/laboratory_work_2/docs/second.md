# Просмотр автогонок и регистрация гонщиков.

### Пользователь должен иметь возможность редактирования и удаления своих регистраций.

###### Модель гонки

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

###### Регистрация пользователя на гонку

```
def regs_for_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    regs = Register.objects.filter(racer=request.user)
    return render(request, "regs_of_user.html", {"regs": regs})

```

###### Удаление пользователем своей регистрации на гонку

```
def reg_delete(request, reg_id):

    reg = get_object_or_404(Register, id=reg_id, racer=request.user)

    if request.method == "POST":
        reg.delete()
        return redirect("your_regs")
    else:
        return render(
            request,
            "reg_delete.html",
            {"reg": reg},
        )
```

###### Страница регистраций

```
{% extends 'base.html' %} {% block content %}

<h2 class="mb-4">Your registrations</h2>

<table class="table table-striped table-hover">
    <thead>
    <tr>
        <th scope="col">Race </th>
        <th scope="col">Date of Race</th>
        <th scope="col">Time</th>
        <th scope="col">Result</th>

    </tr>
    </thead>
    <tbody>
    {% for reg in regs %}
    <tr>
        <td class="align-middle">{{reg.race.name}}</td>
        <td class="align-middle">{{reg.race.when}}</td>
        {% if reg.race.finished %}
        <td class="align-middle">{{reg.time_result}}</td>
        <td class="align-middle">{{reg.result}}</td>
        {% else %}
        <td class="align-middle"> -- </td>
        <td class="align-middle"> -- </td>
        {% endif %}

        <td><a href="{% url 'reg_delete' reg.id %}" class="btn btn-danger">delete</a></td>

    </tr>
    {% endfor %}
    </tbody>
</table>

{% endblock %}
```

###### Страница удаления регистрации

```
{% extends 'base.html' %} {% block content %}

<a href="{% url 'race_detail' reg.race.id %}" class="btn btn-secondary mb-4"
  >Back to race</a
>

<h2>Delete registration</h2>
<div>Race: {{ reg.race.name }}</div>
<div>When: {{ reg.race.when }}</div>

<form method="POST" class="mt-3">
  {% csrf_token %}
  <p>Are you sure you want to delete itt?</p>

  <button type="submit" class="btn btn-danger">Delete</button>
</form>

{% endblock %}

```
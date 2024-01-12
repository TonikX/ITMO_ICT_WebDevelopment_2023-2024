# Лабораторная работа 2: реализация простого сайта средствами DJANGO

## Дисциплина: Основы web-программирования

**Цель:** овладеть практическими навыками и умениями реализации web-сервисов
средствами Django.

**Оборудование:** компьютерный класс.

**Программное обеспечение:** Python 3.6+, Django 3, PostgreSQL \*.

**Практическое задание:** Реализовать сайт используя фреймворк Django 3 и СУБД PostgreSQL \*, в
соответствии с вариантом задания лабораторной работы.

**Вариант 6:**

Табло победителей автогонок
Табло должно отображать информацию об участниках автогонок: ФИО участника,
название команды, описание автомобиля, описание участника, опыт и класс участника.
Необходимо реализовать следующий функционал:

- Регистрация новых пользователей.
- Просмотр автогонок и регистрацию гонщиков. Пользователь должен иметь
  возможность редактирования и удаления своих регистраций.
- Написание отзывов и комментариев к автогонкам. Предварительно
  комментатор должен зарегистрироваться. При добавлении комментариев
  должны сохраняться даты заезда, текст комментария, тип комментария
  (вопрос о сотрудничестве, вопрос о гонках, иное), рейтинг (1-10),
  информация о комментаторе.
- Администратор должен иметь возможность указания времени заезда и
  результата средствами Django-admin.
- В клиентской части должна формироваться таблица всех заездов и
  результатов конкретной гонки.

# Регистрация новых пользователей.

###### Модель пользователя

```
class User(AbstractUser):
    description = models.TextField()
    team = models.CharField(max_length=100)
    rating = models.CharField(max_length=15, choices=(('beginner', 'beginner'), ('middle', 'middle'), ('profy', 'profy')))
    car_num = models.CharField(max_length=30)
    car_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name ='Пользователь'
        verbose_name_plural='Пользователи'
```

###### Модель регистрации

```
class Register(models.Model):
    racer = models.ForeignKey(User, related_name='where_to_drive', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='who_drive', on_delete=models.CASCADE)
    result = models.IntegerField(blank=True, null=True,)
    time_result = models.FloatField(blank=True, null=True,)
    class Meta:
        verbose_name ='Регистация'
        verbose_name_plural='Регистрации'
```

###### Форма регистрации

```
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email",
                  "description", "rating", "team", "car_num", "car_description"]

```

###### Регистрация пользователя

```
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("user_login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})
```

###### Страница регистрации

```
{% extends 'base.html' %} {% block content %}

<h2 class="mb-4">Registration</h2>
<form method="post" class="mb-3">
    {% csrf_token %}
    {{ user_form.as_p }}
    <button type="submit" class="btn btn-primary">Register</button>
</form>
<p>Already have a profile? <a href="{% url 'user_login' %}" class="text-primary">Login</a></p>

{% endblock %}

```

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

# Rомментарии

###### Форма комментария

```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["type", "rating", "message"]

```

###### Модель комментария

```

class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="collaboration",
                            choices=(('collaboration', 'collaboration'),
                                     ('racing', 'racing'),
                                     ('other', 'other')))
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural='Комментарии'
```

###### Детали заезда, добавление комментариев

```
def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)

    if request.method == "POST":
        if "rating" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():

                comment = comment_form.save(commit=False)
                comment.race = race
                comment.writer = request.user
                comment.save()
        else:
            Register.objects.create(racer=request.user, race=race)

        return redirect("race_detail", race_id)

    else:
        has_reg = Register.objects.filter(
           racer__id=request.user.id, race__id=race_id
        ).exists()

        regs = Register.objects.filter(race=race_id).order_by('result')

        comment_form = CommentForm()
        comments = Comment.objects.filter(race=race_id)

        return render(
           request,
           "race_detail.html",
           {
               "race": race,
               "has_no_reg": not has_reg,
               "user": request.user,
               "regs": regs,
               "comments": comments,
               'comment_form': comment_form,
           },
       )


```

# Администрирование.

### Администратор должен иметь возможность указания времени заезда и результата средствами Django-admin.

###### Добавление приложения

```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    ]

```

###### Регистрация моделей admin.py

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Race)
admin.site.register(models.Register)
admin.site.register(models.Comment)

```

###### Добавление страницы администратора

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main_app.urls")),
]
```

###### Создание суперюзера

```
python3 manage.py createsuperuser
```

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

# Лабораторная работа 2

## Задание
Реализовать веб сервис "Список туров туристической фирмы".
Хранится информация о названии тура, турагенстве, описании тура, периоде
проведения тура, условиях оплаты.
Необходимо реализовать следующий функционал:
- Регистрация новых пользователей.
- Просмотр и резервирование туров. Пользователь должен иметь возможность
редактирования и удаления своих резервирований.
- Написание отзывов к турам. При добавлении комментариев, должнысохраняться даты тура, текст комментария, рейтинг (1-10), информация о
комментаторе.
- Администратор должен иметь возможность подтвердить резервирование
тура средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая все
проданные туры по странам.

## Реализация

### Создание проекта
Для начала нам необходимо создать виртуальную среду для Python, установить Django и
создать проект
```sh
python -m venv tours-venv
pip install django
django-admin starproject tours
```

После создания проекта нам необходимо добавить в данный проект приложение, которое мы будем разрабатывать
```sh
./manage.py startapp tours_app
```

### Создание моделей базы данных

`Traveler` модель используется для авторизации пользователей. Мы используем свою модель, чтобы в дальнейшем было легче вносить изменения в модель пользователя
```python
class Traveler(AbstractUser):
    pass
```
Для того, чтобы Django использовал данную модель для входа/регистрации нам необходимо добавить строку в `settings.py`
```python
AUTH_USER_MODEL = "tours_app.Traveler"
```

Модель `Tour` хранит в себе информацию об имене, описании, стране проведения, деталях оплаты и агенстве, которое организовывает данный тур
```python
class Tour(Model):
    name = CharField(max_length=200)
    description = TextField(null=True)
    country = ForeignKey("Country", CASCADE)
    payment_details = TextField()
    tour_agency = ForeignKey("TourAgency", CASCADE)

    def __str__(self) -> str:
        return self.name
```

`TourDate` хранит даты начала и окончания тура, связанные с конкретным туром.
```python
class TourDate(Model):
    tour = ForeignKey(Tour, CASCADE)
    start_date = DateField()
    end_date = DateField()
```

Модель `Reservation` связывает туриста (Traveler) с конкретной датой тура (TourDate). Она содержит информацию о времени бронирования и подтверждения брони.
```python
class Reservation(Model):
    traveler = ForeignKey(Traveler, CASCADE)
    tour_date = ForeignKey(TourDate, CASCADE)
    reserved_at = DateTimeField(auto_now_add=True)
    confirmed = BooleanField(default=False)
```

`Review` позволяет туристам оставлять отзывы о конкретной дате тура. Он содержит комментарий, рейтинг и дату отзыва.
```python
class Review(Model):
    tour_date = ForeignKey(TourDate, CASCADE)
    traveler = ForeignKey(Traveler, CASCADE)
    review_datetime = DateTimeField(auto_now_add=True)
    comment = TextField()
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
```

`TourAgency` хранит информацию об агентствах, предоставляющих туры. Она содержит имя агентства и устанавливает связь "многие ко многим" с моделью `Tour`.
```python
class TourAgency(Model):
    name = CharField(max_length=50)
    tours = ManyToManyField(Tour)
```

Модель `Country` содержит информацию о стране, используемую для указания страны, в которой предлагается тур.
```python
class Country(Model):
    code = CharField(max_length=3)  # iso 3166
    display_name = CharField(max_length=50)
```

Эти модели взаимосвязаны между собой, предоставляя базу данных для отслеживания туров, бронирования, отзывов и информации об агентствах и странах.

### Реализация view

Для пользователя используются несколько различных view, но для примера стоит показать view входа.
Данная функция `login_traveler_view` предназначена для обработки запросов на вход пользователя на сайт в качестве туриста. Она использует форму `LoginForm` для проверки предоставленных учетных данных (логина и пароля) и осуществляет вход пользователя в случае успешной проверки.

```python
class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


def login_traveler_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)
    if request.method == "GET":
        return render(request, join(__BASE_TEMPLATE_PATH, "login.html"), dict(form=form))

    if not form.is_valid():
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))

    cd = form.cleaned_data
    try:
        user = Traveler.objects.get(username=cd["username"])
    except Traveler.DoesNotExist:
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))
    if user.password != cd["password"]:
        return render(request, join(__BASE_TEMPLATE_PATH, "invalid_login.html"))

    login(request, user)
    return redirect(f"/profile/{user.pk}")

```

HTML-шаблон представляет собой страницу входа и использует наследование от базового шаблона `base.html`. Он содержит блоки для заголовка и основного содержимого страницы.
```html
{% extends "base.html" %}

{% block header %}
    <title>Login</title>
{% endblock %}

{% block body %}
    <h1>Login</h1>

    <form method="POST" enctype="multipart/form-data">

        {% csrf_token %}

        {{ form.as_p }}

        <input type="submit" value="Login">
    </form>
{% endblock %}
```

Для резерва определенных дат на тур используется функция `reserve_tour_date_view`

```python
def reserve_tour_date_view(request: HttpRequest, pk: int) -> HttpResponse:
    if (user := request.user).is_anonymous:
        return redirect("/login")

    try:
        tour_date = TourDate.objects.get(pk=pk)
    except Tour.DoesNotExist:
        raise Http404("Tour doesn't exist")

    reservation = Reservation(traveler=user, tour_date=tour_date)
    reservation.save()

    return render(request, join(__BASE_TEMPLATE_PATH, "reserved.html"), dict(user=user, tour_date=tour_date))

```

В случае успешного резерва показывается следующая страница
```html
{% extends "base.html" %}

{% block header %}
    <title>Reserved</title>
{% endblock %}

{% block body %}
    <h3>You reserved {{ tour_date.tour.name }} for {{ tour_date.start_date }}</h3>
    <p>Check your reservations in the profile page</p>
{% endblock %}
```

### Добавления urls

В нашем приложении мы создали различные представления и хотим показывать их при переходе на определенный путь в браузере. Для этого создадим файл `urls.py` со следующим содержанием
```python
from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.create_traveler_view),
    path("login", views.login_traveler_view),
    path("profile/<int:pk>", views.traveler_profile_view),
    path("profile", views.traveler_profile_view),
    path("tours", views.all_tours_view),
    path("reserve/<int:pk>", views.reserve_tour_date_view),
    path("cancel_reservation/<int:pk>", views.cancel_reservation_view),
    path("review_tour/<int:pk>", views.write_tour_review_view),
    path("sold_by_country", views.sold_tour_dates_by_country_view)
]
```

Более того, для успешной работы всех путей нам необходимо подключить данный файл из нашего проекта. Для этого изменим содержимое файла `urls.py` в проекте
```python
urlpatterns = [path("admin/", admin.site.urls), path("", include("tours_app.urls"))]
```


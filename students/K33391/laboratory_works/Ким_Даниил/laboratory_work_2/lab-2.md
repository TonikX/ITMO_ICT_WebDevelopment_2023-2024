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
django-admin starproject lab
```

После создания проекта нам необходимо добавить в данный проект приложение, которое мы будем разрабатывать
```sh
./manage.py startapp tours
```

### Создание моделей базы данных

`Traveler` модель используется для авторизации пользователей. Мы используем свою модель, чтобы в дальнейшем было легче вносить изменения в модель пользователя
```python
class Traveler(AbstractUser):
    pass
```
Для того, чтобы Django использовал данную модель для входа/регистрации нам необходимо добавить строку в `settings.py`
```python
AUTH_USER_MODEL = "tours.Traveler"
```

Модель `Tour` хранит в себе информацию о создателе/владельце, названии, описании, периоде проведения и о деталях оплаты
```python
class Tour(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    period = models.CharField(max_length=100)
    payment_conditions = models.TextField()

    def __str__(self):
        return self.title
```

Модель `Reservation` связывает туриста (Traveler) с конкретным туром (Tour). Она содержит информацию о времени бронирования и подтверждения брони.
```python
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.tour.title}'
```

`Review` позволяет туристам оставлять отзывы о конкретном туре. Он содержит комментарий, рейтинг и дату отзыва.
```python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.tour.title}'
```

Эти модели взаимосвязаны между собой, предоставляя базу данных для отслеживания туров, бронирования, отзывов.

### Реализация view

Для пользователя используются несколько различных view, но для примера стоит показать только несколько.
С помощью декораторов я определяю, что для этого метода требуется быть авторизированным пользователем. Например, для перехода на страницу домой или списка резерваций.
Также тут показан код регистрации, я использовал встроенную форму регистрации. 
Функция `create_tour` доступна только администратору и с помощью нее он без админ панели может создать новый тур.

```python
@login_required(login_url='/login/')
def home(request):
    tours = Tour.objects.all()
    form = ReviewForm()  # Форма для добавления отзыва

    return render(request, 'home.html', {'tours': tours, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@admin_required
def create_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.user = request.user
            tour.save()
            return redirect('home')
    else:
        form = TourForm()
    return render(request, 'tours/create_tour.html', {'form': form})


@login_required(login_url='/login/')
def reservations_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'tours/reservations_list.html', {'reservations': reservations})
```

HTML-шаблон представляет собой страницу входа. Он содержит блоки для заголовка и основного содержимого страницы.
Также есть возможность проверки если список туров пуст.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Our Tours</h1>

    <h2>List of Tours</h2>
    <ul>
        {% for tour in tours %}
            <li>
                {{ tour.title }} - {{ tour.description }}
                <form method="post" action="{% url 'add_review' tour.id %}">
                    {% csrf_token %}
                    {{ form.text }}
                    {{ form.rating }}
                    <button type="submit">Add Review</button>
                </form>
                <a href="{% url 'create_reservation' %}">Reserve Tour</a>
            </li>
        {% empty %}
            <p>No tours available.</p>
        {% endfor %}
    </ul>
</body>
</html>
```

Для резерва определенных дат на тур используется функция `create_reservation`
Тут мы мапим туры по id и создаем новый резерв.

```python
@login_required(login_url='/login/')
def create_reservation(request):
    tours = Tour.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            tour_name = form.cleaned_data['tour']
            tour_id = Tour.objects.get(title=tour_name).pk
            tour = Tour.objects.get(id=tour_id)
            # Создание экземпляра модели Reservation
            reservation = form.save(commit=False)
            print(1)
            reservation.user = request.user
            reservation.tour = tour
            reservation.save()
            return redirect('reservations_list')  # Перенаправление на страницу успешной резервации
    else:
        form = ReservationForm()

    return render(request, 'tours/create_reservation.html', {'form': form, 'tours': tours})
```

В случае успешного резерва показывается следующая страница (список всех резервов)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Список резерваций</title>
</head>
<body>
    <h1>Список ваших резерваций</h1>
    <ul>
        {% for reservation in reservations %}
            <li>
                {{ reservation.tour.title }}
                {% if reservation.confirmed %}
                    (Подтверждено)
                {% else %}
                    (Не подтверждено)
                {% endif %}
                <a href="{% url 'edit_reservation' reservation.id %}">Редактировать</a>
                <a href="{% url 'delete_reservation' reservation.id %}">Удалить</a>
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'create_reservation' %}">Создать новую резервацию</a>
</body>
</html>

```

### Добавления urls

В нашем приложении мы создали различные представления и хотим показывать их при переходе на определенный путь в браузере. Для этого создадим файл `urls.py` со следующим содержанием
```python
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('', views.home, name='home'),
    path('reservations/', views.reservations_list, name='reservations_list'),
    path('reservations/create/', views.create_reservation, name='create_reservation'),
    path('reservations/edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('tours/create', views.create_tour, name='create_tour'),
    path('add_review/<int:tour_id>/', views.add_review, name='add_review'),
    path('tours_with_reservation_count/', views.tours_with_reservation_count, name='tours_with_reservation_count'),
]
```

Более того, для успешной работы всех путей нам необходимо подключить данный файл из нашего проекта. Для этого изменим содержимое файла `urls.py` в проекте
```python
urlpatterns = [path("admin/", admin.site.urls), path("", include("tours.urls"))]
```
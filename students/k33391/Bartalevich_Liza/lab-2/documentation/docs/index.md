# Реализация веб-сервиса для тур-агенств на Django

## 1. Задача

Целью было создать веб-сервис для управления тур-агенством с использованием фреймворка Django. Сервис должен позволять пользователям регистрироваться, просматривать список туров, делать бронирование, писать отзывы и просматривать список купленных туров.

## 2. Как выполнялась работа

- **Начальная настройка**: Создан проект Django под названием `travel_agency` и приложение Django под названием `agency`.
- **Создание моделей**: Определены модели в `models.py` для `Agency` (Агенство), `Tour` (Тур), `Reservation` (Бронирование), `Review` (Отзыв).
- **Функции представления**: Разработаны представления для стартовой страницы, регистрации, списка туров, их бронирование и написания отзывов, а также фильтрация по странам.
- **Сопоставление URL**: Сопоставлены шаблоны URL с функциями представления в `urls.py`.
- **Шаблоны**: Созданы HTML-шаблоны для каждого представления для отображения данных.
- **Стилизация**: Применены стили CSS для минималистичного дизайна всех страниц.
- **Аутентификация пользователей**: Использована встроенная аутентификация пользователей Django для функций регистрации и входа.
- **Динамическое содержимое**: Включена динамическая генерация URL в шаблонах для навигации.

## 3. Фрагменты кода

### Фрагмент из models.py

```python
class Agency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def str(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=200)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='tours')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.CharField(max_length=200)
    payment_conditions = models.TextField()

    def str(self):
        return self.name
```

### Фрагмент из views.py

```python
@login_required
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})


@login_required
def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})

```

### Фрагмент из reserve_tour.html

```html
{% extends 'base.html' %} {% block content %}
<h2>Забронировать тур: {{ tour.name }}</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Reserve</button>
</form>
{% endblock %}
```

### Фрагмент из urls.py

```python
urlpatterns = [
    path('register/', views.register, name='register'),
    path('agency/', views.tour_list, name='tour_list'),
    path('agency/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('agency/<int:tour_id>/reserve/', views.reserve_tour, name='reserve_tour'),
    path('agency/<int:tour_id>/comment/', views.tour_detail, name='tour_comment'),
    path('tours_by_country/', views.tours_by_country_view, name='tours_by_country'),
]
```

## 4. Краткий вывод

Лабораторная была выполнена успешно, демонстрируя возможности Django для быстрой разработки и его мощную ORM для взаимодействия с базой данных. Теперь, когда у нас установлена надежная база, веб-сервис обеспечивает легкую навигацию, делая пользовательский опыт плавным и интуитивно понятным.

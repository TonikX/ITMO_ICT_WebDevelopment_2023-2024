# Лабораторная работа 2

**РЕАЛИЗАЦИЯ ПРОСТОГО САЙТА СРЕДСТВАМИ DJANGO**

## Intro

**Цель:** овладеть практическими навыками и умениями реализации web-сервисов
средствами Django 2.2.

**Оборудование:** компьютерный класс.

**Программное обеспечение:** Python 3.6+, Django 3, PostgreSQL *.

**Практическое задание:** Реализовать сайт используя фреймворк Django 3 и СУБД PostgreSQL *, в
соответствии с вариантом задания лабораторной работы.

**Вариант: 4**

**Задание: Список туров туристической фирмы**

Хранится информация о названии тура, турагенстве, описании тура, периоде проведения тура, условиях оплаты.
Необходимо реализовать следующий функционал:

- Регистрация новых пользователей.
- Просмотр и резервирование туров. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
- Написание отзывов к турам. При добавлении комментариев, должны сохраняться даты тура, текст комментария, рейтинг (1-10), информация о комментаторе.
- Администратор должен иметь возможность подтвердить резервирование тура средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая все проданные туры по странам.

## models

В файле models.py у нас 4 модели для реализации основного функционала. 

    from django.db import models
    from django.contrib.auth.models import User

    class Tour(models.Model):
        title = models.CharField(max_length=100)
        agency = models.CharField(max_length=100)
        description = models.TextField()
        start_date = models.DateField()
        end_date = models.DateField()
        payment_conditions = models.TextField()
        is_sold = models.BooleanField(default=False)

**Tour** – содержит информацию о турах: название, агенство, которое предоставляет услугу, описание тура, даты начала и конца, способ оплаты и статус "продано" или нет;

    class Reservation(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

**Reservation** – содержит информацию о пользователе и его резервировании;

    class Review(models.Model):
        tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField()
        rating = models.PositiveIntegerField()
        date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Review for {self.tour.name} by {self.user.username}"

**Review** – содержит информацию об отзывах: тур, имя пользователя, его оценка и комментарий и дата написания отзыва;

    class Country(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name

**Country** – содержит информацию о стране тура.


## forms

**Формы для оставления отзывов и бронирования**

    from django import forms
    from .models import Review
    from .models import Reservation

    class ReviewForm(forms.ModelForm):
        class Meta:
            model = Review
            fields = ['text', 'rating']

    class ReservationForm(forms.ModelForm):
        class Meta:
            model = Reservation
            fields = ['user', 'tour']

**html – код отображения поля для ввода отзыва**

    {% extends "base.html" %}

    {% block content %}
        <div class="container">
        <h2>Write a Review for {{ tour.name }}</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Submit Review</button>
        </form>
        </div>
    {% endblock %}

![Review](Lab1.2.png)

**html – код отображения поля для брони**

    {% extends "base.html" %}

    {% block content %}
    <h2>Reserve Tour - {{ tour.name }}</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Reserve</button>
    </form>
    <a href="{% url 'tour_list' %}">Back to Tour List</a>
    {% endblock %}

## views

    from .forms import ReviewForm
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    from django.db.models import Count
    from .models import Country, Tour
    from django.shortcuts import render, redirect,  get_object_or_404
    from .models import Reservation
    from .forms import ReservationForm

    def tour_list(request):
        tours = Tour.objects.all()
        return render(request, '/Users/marinakuzmina/Documents/weblab2/tour_project/templates/tour_list.html', {'tours': tours})

    def tour_detail(request, tour_id):
        tour = Tour.objects.get(pk=tour_id)
        return render(request, '/Users/marinakuzmina/Documents/weblab2/tour_project/templates/tour_detail.html', {'tour': tour})

    def reserve_tour(request, tour_id):
        if request.user.is_authenticated:
            tour = Tour.objects.get(pk=tour_id)
            reservation = Reservation(user=request.user, tour=tour)
            reservation.save()
            return redirect('user_profile')
        else:
            return redirect('login')


    def write_review(request, tour_id):
        tour = Tour.objects.get(pk=tour_id)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.tour = tour
                review.user = request.user
                review.save()
                return redirect('tour_detail', tour_id=tour_id)
        else:
            form = ReviewForm()

        return render(request, '/Users/marinakuzmina/Documents/weblab2/tour_project/templates/write_review.html', {'form': form, 'tour': tour})


    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('tour_list')  # Перенаправление на главную страницу после регистрации
        else:
            form = UserCreationForm()
        return render(request, '/Users/marinakuzmina/Documents/weblab2/tour_project/templates/registration/registration.html', {'form': form})

    def sold_tours_by_country(request):
        sold_tours = Tour.objects.filter(is_sold=True)
        return render(request, 'sold_tours_by_country.html', {'sold_tours': sold_tours})


    def user_profile(request):
        if request.user.is_authenticated:
            user_reservations = Reservation.objects.filter(user=request.user)

            return render(request, 'user_profile.html', {'user_reservations': user_reservations})
        else:
            return redirect('login')

    def update_reservation(request, reservation_id):
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
        except Reservation.DoesNotExist:
            return redirect('error_page')  # Обработка несуществующей резервации

        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reservation)  # Указываем экземпляр для обновления
            if form.is_valid():
                form.save()  # Сохраняем обновленную резервацию
                return redirect('user_profile')  # Перенаправляем на страницу профиля или другую страницу
        else:
            form = ReservationForm(instance=reservation)  # Передаем экземпляр для отображения данных в форме

        return render(request, 'update_reservation.html', {'form': form, 'reservation': reservation})

    def delete_reservation(request, reservation_id):
        reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)

        if request.method == 'POST':
            reservation.delete()
            return redirect('user_profile')

        return render(request, 'delete_reservation.html', {'reservation': reservation})

## urls

    from django.urls import path
    from tour_project import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', views.tour_list, name='tour_list'),
        path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
        path('tour/<int:tour_id>/reserve/', views.reserve_tour, name='reserve_tour'),
        path('tour/<int:tour_id>/write_review/', views.write_review, name='write_review'),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('register/', views.register, name='register'),
        path('profile/', views.user_profile, name='user_profile'),
        # URL-маршруты для обновления и удаления резерваций
        path('reservation/update/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
        path('reservation/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
        path('sold_tours_by_country/', views.sold_tours_by_country, name='sold_tours_by_country'),
    ]

## Выводы

В рамках второй лабораторной работы "РЕАЛИЗАЦИЯ ПРОСТОГО САЙТА СРЕДСТВАМИ DJANGO" было изучено использование django: проектирование базы данных, создание представлений и основы html – верстки. 
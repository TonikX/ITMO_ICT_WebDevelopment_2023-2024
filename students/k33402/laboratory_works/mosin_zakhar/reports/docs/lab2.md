# ЛАБОРАТОРНАЯ РАБОТА №2 : Реализация Простого Сайта Средствами Django #
**Цель:** Овладеть практическими навыками и умениями реализации web-сервисов средствами Django 2.2.

## Выполнение работы ##
### Вариант 1: Список отелей ###
Необходимо учитывать название отеля, владельца отеля, адрес, описание, типы номеров, стоимость, вместимость, удобства. 
Необходимо реализовать следующий функционал:

* Регистрация новых пользователей.
* Просмотр и резервирование номеров. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
* Написание отзывов к номерам. При добавлении комментариев, должны сохраняться период проживания, текст комментария, рейтинг (1-10), информация о комментаторе.
* Администратор должен иметь возможность заселить пользователя в отель и выселить из отеля средствами Django-admin. 
* В клиентской части должна формироваться таблица, отображающая постояльцев отеля за последний месяц.

admin.py
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.Passenger, UserAdmin)
admin.site.register(models.City)
admin.site.register(models.Hotel)
admin.site.register(models.TypeOfRoom)
admin.site.register(models.Room)
admin.site.register(models.Reservation)
admin.site.register(models.Comment)
```

apps.py
```python
from django.apps import AppConfig


class FlightsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hotels"
```

forms.py
```python
from django import forms
from .models import Passenger, Reservation, Comment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password", "first_name", "last_name", "email", "passport"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["room", "date_start", "date_finish"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["rating", "text"]
```

models.py
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class City(models.Model):
    name = models.CharField(max_length=1000)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=200)
    city = models.ForeignKey("hotels.City", related_name="hotels_there", on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class TypeOfRoom(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    conveniences = models.CharField(max_length=1000)
    cost = models.FloatField()


class Room(models.Model):
    hotel = models.ForeignKey("hotels.Hotel", related_name="rooms", on_delete=models.CASCADE)
    type = models.ForeignKey("hotels.TypeOfRoom", related_name="rooms_of_this_type", on_delete=models.CASCADE)
    number = models.CharField(max_length=10)


class Reservation(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_reservations", on_delete=models.CASCADE)
    room = models.ForeignKey("hotels.Room", related_name="reserved_by", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class Passenger(AbstractUser):
    passport = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.passport}"

```

urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="logout"),

    path("hotels", views.hotel_list, name="hotel_list"),
    path("hotels/<int:hotel_id>", views.hotel_detail, name="hotel_detail"),
    path("hotels/<int:hotel_id>/reserve", views.reserve_room, name="reserve_room"),

    path("reservations/", views.reservations_for_user, name="reservations_for_user"),
    path("reservations/<int:reservation_id>/", views.reservation_update, name="reservation_update"),
    path("reservations/<int:reservation_id>/delete", views.reservation_delete, name="reservation_delete"),

]
```

views.py
```python
import datetime
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from .forms import ReservationForm, RegistrationForm, LoginForm, CommentForm
from .models import TypeOfRoom, Room, Reservation, Hotel, Comment, City
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


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


def user_login(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)

        username = user_form.data.get("username")
        password = user_form.data.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect("user_login")

        login(request, user)
        return redirect("hotel_list")
    else:
        user_form = LoginForm()

    return render(request, "login.html", {"user_form": user_form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


def hotel_list(request):

    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    capacity = request.GET.get("capacity", None)
    city = request.GET.get("city", None)

    available_capacities = TypeOfRoom.objects.values_list("capacity", flat=True)
    available_cities = City.objects.values_list("name", flat=True)

    hotels = Hotel.objects.all()

    if capacity is not None:
        hotels = hotels.filter(rooms__type__capacity__gte=capacity)

    if city is not None:
        hotels = hotels.filter(city__name=city)

    return render(
        request,
        "list.html",
        {
            "capacity": capacity,
            "city": city,
            "available_capacities": available_capacities,
            "available_cities": available_cities,
            "hotels": hotels
        },
    )


def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if Reservation.objects.filter(passenger=request.user, room__hotel=hotel_id).exists():
                comment = comment_form.save(commit=False)
                comment.hotel = Hotel.objects.get(id=hotel_id)
                comment.author = request.user
                comment.save()
        return redirect("hotel_detail", hotel_id)

    else:
        rooms_set = Room.objects.filter(hotel__id=hotel_id).order_by("number")
        rooms = []

        for room in rooms_set:
            if not (Reservation.objects.filter(room=room, date_start__lte=datetime.date.today(),
                                               date_finish__gte=datetime.date.today()).exists()):
                rooms.append(
                    {
                       "name": f"{room.number}",
                       "capacity": f"{room.type.capacity}",
                       "conveniences": f"{room.type.conveniences}",
                       "cost": f"{room.type.cost}"
                   }
                )

        comments = Comment.objects.filter(hotel=hotel)
        comment_form = CommentForm()

        return render(
           request,
           "detail.html",
           {
               "hotel": hotel,
               "comments": comments,
               "comments_exists": bool(comments.count()),
               "rooms": rooms,
               "user": request.user,
               "comment_form": comment_form
           },
       )


@login_required(login_url="/login/")
def reserve_room(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == "POST":
        room = Room.objects.filter(number=request.POST["room"]).first()
        try:
            date_start = datetime.datetime.strptime(request.POST["date-start"], "%d.%m.%Y")
            date_finish = datetime.datetime.strptime(request.POST["date-finish"], "%d.%m.%Y")

            form = ReservationForm({"room": room, "date_start": date_start, "date_finish": date_finish})

            if not form.is_valid():
                return redirect("hotel_detail", hotel_id)

            reservation = form.save(commit=False)
            reservation.passenger = request.user
            reservation.room = room
            reservation.save()

        except Exception:
            return redirect("hotel_detail", hotel_id)

        return redirect("hotel_detail", hotel_id)

    else:
        return render(request, "reserve_room.html", {"form" : ReservationForm(), "hotel": hotel})


@login_required(login_url="/login/")
def reservations_for_user(request):
    reservations = Reservation.objects.filter(passenger=request.user)
    return render(request, "reservation_for_user.html", {"reservations": reservations})


def reservation_update(request, reservation_id):

    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        form = ReservationForm(data=request.POST, instance=reservation)
        if not form.is_valid():
            return redirect("reservation_update", reservation_id)

        form.save()
        return redirect("hotel_detail", reservation.room.hotel.id)
    else:
        form = ReservationForm(instance=reservation)
        return render(
            request,
            "reservation_update.html",
            {"form": form, "reservation": reservation},
        )


@login_required(login_url="/login/")
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, passenger=request.user)

    if request.method == "POST":
        reservation.delete()
        return redirect("hotel_detail", reservation.room.hotel.id)
    else:
        return render(
            request,
            "reservation_delete.html",
            {"reservation": reservation},
        )
```
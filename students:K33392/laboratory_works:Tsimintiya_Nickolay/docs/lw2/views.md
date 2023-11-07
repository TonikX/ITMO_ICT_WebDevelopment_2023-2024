# Представления
Представления в Django —это то, что в классическом паттерне MVC называется контроллерами. Это место, где происходит обработка запросов и формирование ответов. Они определяются в файле views.py.

В рамках данной лабораторной работы структура этого файла следующая:

``` Python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, ReservationForm, ReviewForm
from .models import Hotel, RoomType, Reservation, Review
from datetime import datetime, timedelta


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hotel_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})


def room_reserve(request, hotel_id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('hotel_list')
    else:
        form = ReservationForm()
        form.fields['room_type'].queryset = RoomType.objects.filter(hotel_id=hotel_id)
    return render(request, 'room_reserve.html', {'form': form})


def write_review(request, hotel_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.room_type = RoomType.objects.filter(hotel_id=hotel_id).first()
            review.save()
            return redirect('hotel_list')
    else:
        form = ReviewForm()
    return render(request, 'write_review.html', {'form': form})


def last_month_guests(request):
    one_month_ago = datetime.today() - timedelta(days=30)
    reservations = Reservation.objects.filter(start_date__gte=one_month_ago)
    return render(request, 'last_month_guests.html', {'reservations': reservations})
```
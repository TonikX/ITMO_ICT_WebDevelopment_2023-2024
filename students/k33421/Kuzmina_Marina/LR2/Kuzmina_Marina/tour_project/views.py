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

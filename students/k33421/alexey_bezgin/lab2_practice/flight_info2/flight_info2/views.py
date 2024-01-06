from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import ReservationForm, ReviewForm
from .models import Reservation, Flight, Review


def home(request):
    return render(request, 'home.html')


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/personal_space/')  # Redirect to the home page or any other desired page.
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/personal_space/')  # Redirect to the home page or any other desired page.
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the home page or any other desired page.


@login_required
def personal_space_view(request):
    username = request.user.username
    return render(request, 'personal_space.html', {'username': username})


# просмотр списка броней
@login_required
def show_user_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'user_reservations.html', {'reservations': reservations})


@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form})


@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('user_reservations')
    return render(request, 'delete_reservation.html', {'reservation': reservation})


@user_passes_test(lambda u: u.is_superuser)
def flight_passengers(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    reservations = Reservation.objects.filter(flight=flight)
    return render(request, 'flight_passengers.html', {'flight': flight, 'reservations': reservations})


# ...
@login_required
def create_review(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.flight = flight
            review.user = request.user
            review.date = timezone.now()  # Set the date field manually
            review.save()
            return redirect('flight_reviews', flight_id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'flight': flight})


def flight_reviews(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    reviews = Review.objects.filter(flight=flight)
    return render(request, 'show_flight_reviews.html', {'flight': flight, 'reviews': reviews})


def flights_list(request):
    flights = Flight.objects.all()
    return render(request, 'all_flights_list.html', {'flights': flights})

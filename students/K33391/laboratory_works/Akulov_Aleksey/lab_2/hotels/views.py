from datetime import timezone, timedelta, datetime

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from django.shortcuts import redirect, render, get_object_or_404

from .models import Hotel, Reservation
from .forms import VisitorCreationForm, ReservationForm


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})


def register(request):
    if request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hotel_list')
    else:
        form = VisitorCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html',
                  {'reservations': reservations})


@login_required
def reservation_edit(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id,
                                    user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation_edit.html',
                  {'form': form, 'reservation': reservation})


@login_required
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation,
                                    pk=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation_delete.html',
                  {'reservation': reservation})


def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_admin)
def admin_reservation_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    reservation = Reservation.objects.filter(user=user)
    return render(request, 'admin_reservations_list.html',
                  {'reservation': reservation, 'reserved_user': user})


# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Reservation, Review
from .forms import ReviewForm


@login_required
def review(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.user != reservation.user:
        return redirect('reservation_list')

    review, created = Review.objects.get_or_create(
        reservation=reservation,
        defaults={
            'author': request.user,
            'rating': 10,
            'stay_from': reservation.start_date,
            'stay_to': reservation.end_date,
        }
    )

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            if created:
                review = form.save(commit=False)
                review.author = request.user
                review.save()
            else:
                form.save()
            return redirect('reservation_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review.html',
                  {'form': form, 'reservation': reservation})


def hotel_guests(request):
    today = datetime.now().date()
    first_day = today.replace(day=1)

    reservations_last_month = Reservation.objects.filter(
        start_date__gte=first_day)

    hotels_with_guests = {}
    for reservation in reservations_last_month:
        hotel_name = reservation.room_type.hotel.name
        if hotel_name not in hotels_with_guests:
            hotels_with_guests[hotel_name] = []
        hotels_with_guests[hotel_name].append(reservation)

    return render(request, 'hotel_guests.html',
                  {'hotels_with_guests': hotels_with_guests})

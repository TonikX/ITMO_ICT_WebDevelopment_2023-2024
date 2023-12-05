import datetime

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from flight_management.forms import CustomUserCreationForm, FlightReviewForm, FlightSeatForm
from .models import Flight, Passenger, Reservation, FlightReview


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    reservations = Reservation.objects.filter(passenger=user.passenger)
    context = {
        'user': user,
        'reservations': [(reservation.flight, reservation.seat_number) for reservation in reservations],
    }

    return render(request, 'profile.html', context)


def flight_detail_view(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    reviews = FlightReview.objects.filter(flight=flight)

    reserved_seats = Reservation.objects.filter(flight=flight).values_list('seat_number', flat=True)
    total_seats = range(1, flight.total_seats + 1)

    seat_form = FlightSeatForm()
    error_message = None

    if request.method == 'POST':
        form = FlightReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.flight = flight
            review.commentator = request.user.passenger
            review.date = datetime.date.today()
            review.save()
            return redirect('flight_detail', flight_id=flight_id)
        elif request.user.is_authenticated:
            passenger = request.user.passenger
            if not Reservation.objects.filter(passenger=passenger, flight=flight).exists():
                seat_form = FlightSeatForm(request.POST)
                if seat_form.is_valid():
                    reservation = seat_form.save(commit=False)
                    reservation.passenger = passenger
                    reservation.flight = flight
                    reservation.save()
                    return redirect('flight_detail', flight_id=flight_id)
            else:
                error_message = "You're already registered for this flight."
    else:
        form = FlightReviewForm()

    return render(request, 'flight_detail.html', {
        'flight': flight,
        'reviews': reviews,
        'form': form,
        'seat_form': seat_form,
        'reserved_seats': reserved_seats,
        'total_seats': total_seats,
        'error_message': error_message if 'error_message' in locals() else None,
    })


def view_flights(request):
    flights = Flight.objects.all()

    current_passenger = None
    if request.user.is_authenticated:
        try:
            current_passenger = Passenger.objects.get(user=request.user)
        except Passenger.DoesNotExist:
            pass

    return render(request, 'view_flights.html', {'flights': flights, 'current_passenger': current_passenger})


@login_required
def cancel_registration(request, flight_id):
    current_passenger = None
    if request.user.is_authenticated:
        try:
            current_passenger = Passenger.objects.get(user=request.user)
        except Passenger.DoesNotExist:
            pass

    flight = Flight.objects.get(id=flight_id)
    reservation = Reservation.objects.filter(passenger=current_passenger, flight=flight)
    print(reservation)

    if reservation:
        for res in reservation:
            res.delete()
    return redirect('profile')

from typing import NamedTuple

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RegisterForm, ReservationForm, ReviewForm
from .models import Flight, Reservation


def index(request):
    flight_list: QuerySet[Flight] = Flight.objects.order_by("id")[:10]
    return render(request, 'index.html', {'flight_list': flight_list})


def home_redirect(request):
    return redirect('/airport')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/airport')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def flight_info(request, flight_id):
    flight: Flight = get_object_or_404(Flight, pk=flight_id)
    dtos = []
    for passenger in flight.passengers.all():
        dtos.append(PassengerDTO(
            passenger.first_name + ' ' + passenger.last_name,
            Reservation.objects.filter(passenger=passenger.id).get().seat_number,
            Reservation.objects.filter(passenger=passenger.id).get().checked_in
        ))
    return render(request, 'flight_info.html', {
        'dtos': dtos,
        'flight_number': flight.flight_number,
        'flight_id': flight.id
    })


def list_reservations(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(passenger=request.user.id)
        return render(request, 'reservation_list.html', context={'reservations': reservations})
    else:
        return HttpResponse('Please sign in to view your reservations.')


def delete_reservation(request, reservation_id):
    if request.user.is_authenticated:
        get_object_or_404(Reservation, pk=reservation_id).delete()
        return redirect('/airport/list_reservations')
    else:
        return HttpResponse('Please sign in to manage your reservations.')


def make_reservation(request, flight_id, reservation_id=None):
    if request.user.is_authenticated:
        if request.method == 'POST':
            flight = get_object_or_404(Flight, pk=flight_id)
            if reservation_id is None:
                form = ReservationForm(request.POST)
                if form.is_valid():
                    new_res = form.save(commit=False)
                    new_res.flight = flight
                    new_res.passenger = request.user
                    new_res.save()
                    return redirect('/airport/list_reservations')
            else:
                reservation = get_object_or_404(Reservation, pk=reservation_id)
                form = ReservationForm(request.POST, instance=reservation)
                form.save()
                return redirect('/airport/list_reservations')
        else:
            form = ReservationForm()
        return render(request,
                      'make_reservation.html',
                      {'form': form, 'flight_id': flight_id, 'reservation_id': reservation_id})
    else:
        return HttpResponse('Please sign in to manage your reservations.')


def make_review(request, flight_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            flight = get_object_or_404(Flight, pk=flight_id)
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_res = form.save(commit=False)
                new_res.flight = flight
                new_res.passenger = request.user
                new_res.save()
                return redirect('/airport/list_reservations')
        else:
            form = ReviewForm()
        return render(request, 'make_review.html', {'form': form, 'flight_id': flight_id})
    else:
        return HttpResponse('Please sign in to manage your reservations.')


class PassengerDTO(NamedTuple):
    full_name: str
    seat: str
    checked_in: bool

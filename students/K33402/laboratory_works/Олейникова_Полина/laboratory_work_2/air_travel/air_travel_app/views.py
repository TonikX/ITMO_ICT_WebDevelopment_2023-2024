from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.contrib.auth import logout
from datetime import date, datetime
from .models import Flight, Reservation, Comment
from .forms import (RegistrationForm, ReservationForm, CommentForm)


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})


def user_logout(request):
    logout(request)
    return redirect("login")


def flights_list(request):
    flights = Flight.objects.all()
    return render(request, "flights_list.html", {"flights": flights})


def flight_info(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    passengers = list(map(lambda r: r.passenger, Reservation.objects.filter(flight=flight)))
    is_available = flight.departure.date() > datetime.today().date()
    if request.user.is_authenticated:
        is_register = request.user in passengers
        try:
            reservation = Reservation.objects.get(flight=flight, passenger=request.user)
        except Reservation.DoesNotExist:
            reservation = None
    else:
        is_register = False
        reservation = None

    comments = Comment.objects.filter(flight=flight)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.flight = flight
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()
    return render(
        request,
        "flight_info.html",
        {"flight": flight,
         "comments": comments,
         "passengers": passengers,
         "is_register": is_register,
         "reservation": reservation,
         "is_available": is_available,
         "form": form},
    )


@login_required(login_url='/login/')
def reservations_for_user(request):
    reservations = Reservation.objects.filter(passenger=request.user)
    return render(request, "reservations_for_user.html", {"reservations": reservations})


@login_required(login_url='/login/')
def reservation_create(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if flight.departure.date() <= datetime.today().date():
        raise Http404(f"Reservation ended")

    user = request.user
    if request.method == "POST":
        reservation_form = ReservationForm(flight.id, request.POST)
        if reservation_form.is_valid():
            user_reservation = reservation_form.save(commit=False)
            user_reservation.passenger = user
            user_reservation.flight = flight
            user_reservation.ticket_number = get_random_string(length=32)
            user_reservation.date = date.today()
            user_reservation.save()
            return redirect("flight_info", flight.id)
    else:
        reservation_form = ReservationForm(flight.id)

    return render(
        request,
        "reservation.html",
        {"form": reservation_form, "flight": flight},
    )


@login_required(login_url='/login/')
def reservation_update(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, passenger=request.user)

    if reservation.flight.departure.date() <= datetime.today().date():
        raise Http404(f"Reservation ended")

    if request.method == "POST":
        form = ReservationForm(reservation.flight.id, request.POST, instance=reservation)
        if not form.is_valid():
            return redirect("reservation_update", reservation_id)

        form.save()
        return redirect("flight_info", reservation.flight.id)
    else:
        form = ReservationForm(reservation.flight.id, instance=reservation)
        return render(
            request,
            "reservation_update.html",
            {"form": form, "reservation": reservation},
        )


@login_required(login_url='/login/')
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, passenger=request.user)

    if reservation.flight.departure.date() <= datetime.today().date():
        raise Http404(f"Reservation ended")

    if request.method == "POST":
        reservation.delete()
        return redirect("flight_info", reservation.flight.id)
    else:
        return render(
            request,
            "reservation_delete.html",
            {"reservation": reservation},
        )


def custom_404(request):
    return render(request, '404.html', status=404)

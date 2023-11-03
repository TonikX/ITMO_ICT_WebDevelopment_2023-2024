from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from .forms import ReservationForm, RegistrationForm, LoginForm, CommentForm
from .models import Flight, City, Reservation, Seat, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.db.models import Q


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
        return redirect("flights_list")
    else:
        user_form = LoginForm()

    return render(request, "login.html", {"user_form": user_form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


# Create your views here.
def flights_list(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    city = request.GET.get("city", None)
    available_cities = City.objects.all()

    flights = Flight.objects.all()

    if city is not None:
        flights.filter(Q(arrival_city__name=city) or Q(departure_city__name=city))

    return render(
        request,
        "flight_list.html",
        {
            "city": city,
            "available_cities": available_cities,
            "flights": flights
        },
    )


def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("user_login")

        if 'seat' in request.POST.keys():
            seat = Seat.objects.filter(row=request.POST['seat'][0], column=request.POST['seat'][1]).first()
            form = ReservationForm({"seat": seat})
            if not form.is_valid():
                return redirect("flight_detail", flight_id)
            ticket = form.save(commit=False)
            ticket.passenger = request.user
            ticket.flight = flight
            ticket.ticken_number = get_random_string(32)
            ticket.save()
        elif "rating" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.flight = flight
                comment.author = request.user
                comment.save()

        return redirect("flight_detail", flight_id)

    else:
        seats_set = Seat.objects.filter(plane__plane_flights__id=flight_id).order_by("row", "column")
        seats = [
               {
                   "name": f"{seat}",
                   "is_taken": Reservation.objects.filter(seat__id=seat.id, flight__id=flight_id).exists(),
               } for seat in seats_set
        ]

        reseravtion_form = ReservationForm(flight)

        has_ticket = Reservation.objects.filter(
           passenger__id=request.user.id, flight__id=flight.id
        ).exists()

        comments = Comment.objects.filter(flight=flight)
        comment_form = CommentForm()

        return render(
           request,
           "flight_detail.html",
           {
               "flight": flight,
               "comments": comments,
               "tickets": Reservation.objects.filter(flight__id=flight_id),
               "seats": seats,
               "form": reseravtion_form,
               "has_ticket": has_ticket,
               "user": request.user,
               "comment_form": comment_form
           },
       )


@login_required(login_url='/login/')
def reservations_for_user(request):
    reservations = Reservation.objects.filter(passenger=request.user)
    return render(request, "reservation_for_user.html", {"reservations": reservations})


def reservation_update(request, reservation_id):

    reservation = get_object_or_404(Reservation, id=reservation_id)

    #if reservation.flight.departure_time.date() <= datetime.today().date():
    #    raise Http404(f"Reservation ended")

    if request.method == "POST":
        form = ReservationForm(reservation.flight.id, request.POST, instance=reservation)
        if not form.is_valid():
            return redirect("reservation_update", reservation_id)

        form.save()
        return redirect("flight_detail", reservation.flight.id)
    else:
        form = ReservationForm(instance=reservation)
        return render(
            request,
            "reservation_update.html",
            {"form": form, "reservation": reservation},
        )


@login_required(login_url='/login/')
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, passenger=request.user)

    #if reservation.flight.departure_time.date() <= datetime.today().date():
    #    raise Http404(f"Reservation ended")

    if request.method == "POST":
        reservation.delete()
        return redirect("flight_detail", reservation.flight.id)
    else:
        return render(
            request,
            "reservation_delete.html",
            {"reservation": reservation},
        )
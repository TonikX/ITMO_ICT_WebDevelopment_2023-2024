from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from string import ascii_uppercase
from django.contrib import messages

from .models import Flight, City, Ticket
from .forms import UserRegisterForm, TicketForm


def index(request):
    messages.success(request, "Информация обновлена!")
    return render(request, "air_tickets_booking/index.html", {"user": request.user})


def user_register_view(request):
    match request.method:
        case "POST":
            form = UserRegisterForm(request.POST)
            if not form.is_valid():
                return redirect("user_register")

            user = form.save()
            login(request, user)
            return redirect("index")

        case "GET":
            form = UserRegisterForm()
            return render(
                request, "air_tickets_booking/user_register.html", {"form": form}
            )

        case _:
            return Http404(f"Method {request.method} not supported")


def user_login_view(request):
    match request.method:
        case "POST":
            form = AuthenticationForm(request, request.POST)
            if not form.is_valid():
                return redirect("user_login")

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is None:
                return redirect("user_login")

            login(request, user)
            return redirect("index")

        case "GET":
            form = AuthenticationForm()
            return render(
                request, "air_tickets_booking/user_login.html", {"form": form}
            )

        case _:
            return Http404(f"Method {request.method} not supported")


def user_logout(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    logout(request)
    return redirect("index")


def flights_list_view(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    city = request.GET.get("city", None)
    available_cities = City.objects.all()
    flights_out = None
    flights_in = None

    if city is not None:
        flights_out = Flight.objects.filter(departure_city__name=city)
        flights_in = Flight.objects.filter(arrival_city__name=city)

    return render(
        request,
        "air_tickets_booking/flights_list.html",
        {
            "city": city,
            "available_cities": available_cities,
            "flights_out": flights_out,
            "flights_in": flights_in,
        },
    )


def flight_detail_view(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    match request.method:
        case "POST":
            if not request.user.is_authenticated:
                return redirect("user_login")

            form = TicketForm(request.POST)
            if not form.is_valid():
                return redirect("flight_detail", flight_id)

            if Ticket.objects.filter(
                passenger__id=request.user.id, flight__id=flight.id
            ).exists():
                return redirect("flight_detail", flight_id)

            ticket = form.save(commit=False)
            ticket.passenger = request.user
            ticket.flight = flight
            ticket.save()

            return redirect("flight_detail", flight_id)

        case "GET":
            tickets = Ticket.objects.filter(flight__id=flight_id)
            seats_set = {ticket.seat for ticket in tickets}
            seats = [
                [
                    {
                        "name": f"{row+1}{ascii_uppercase[seat]}",
                        "is_taken": f"{row+1}{ascii_uppercase[seat]}" in seats_set,
                    }
                    for seat in range(flight.plane.columns)
                ]
                for row in range(flight.plane.rows)
            ]

            form = TicketForm()
            has_ticket = Ticket.objects.filter(
                passenger__id=request.user.id, flight__id=flight.id
            ).exists()
            return render(
                request,
                "air_tickets_booking/flight_detail.html",
                {
                    "flight": flight,
                    "tickets": tickets,
                    "seats": seats,
                    "form": form,
                    "has_ticket": has_ticket,
                    "user": request.user,
                },
            )

        case _:
            return Http404(f"Method {request.method} not supported")


@login_required
def tickets_list_view(request):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    tickets = Ticket.objects.filter(passenger__id=request.user.id)
    return render(
        request,
        "air_tickets_booking/tickets_list.html",
        {"tickets": tickets},
    )


@login_required
def ticket_update_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id, passenger__id=request.user.id)
    match request.method:
        case "POST":
            form = TicketForm(request.POST, instance=ticket)
            if not form.is_valid():
                return redirect("ticket_update", ticket_id)

            form.save()
            return redirect("tickets_list")

        case "GET":
            form = TicketForm(instance=ticket)
            return render(
                request,
                "air_tickets_booking/ticket_update.html",
                {"form": form, "ticket": ticket},
            )

        case _:
            return Http404(f"Method {request.method} not supported")


@login_required
def ticket_delete(request, ticket_id):
    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    ticket = get_object_or_404(Ticket, pk=ticket_id, passenger__id=request.user.id)
    ticket.delete()
    return redirect("tickets_list")

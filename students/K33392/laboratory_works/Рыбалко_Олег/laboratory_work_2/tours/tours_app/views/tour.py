from os.path import join

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from tours_app.models import Reservation, Tour

__BASE_TEMPLATE_PATH = "tour"


def all_tours_view(request: HttpRequest) -> HttpResponse:
    return render(request, join(__BASE_TEMPLATE_PATH, "all.html"), dict(tours=Tour.objects.all()))


def reserve_tour_view(request: HttpRequest, pk: int) -> HttpResponse:
    if (user := request.user).is_anonymous:
        return redirect("/login")

    try:
        tour = Tour.objects.get(pk=pk)
    except Tour.DoesNotExist:
        raise Http404("Tour doesn't exist")

    reservation = Reservation(traveler=user, tour=tour)
    reservation.save()

    return render(request, join(__BASE_TEMPLATE_PATH, "reserved.html"), dict(user=user, tour=tour))


def cancel_reservation_view(request: HttpRequest, pk: int) -> HttpResponse:
    if (user := request.user).is_anonymous:
        return redirect("/login")

    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        raise Http404("Reservation doesn't exist")

    if reservation.traveler.pk != user.pk:
        raise HttpResponseForbidden("It's not your reservation")

    reservation.delete()

    return redirect("/profile")

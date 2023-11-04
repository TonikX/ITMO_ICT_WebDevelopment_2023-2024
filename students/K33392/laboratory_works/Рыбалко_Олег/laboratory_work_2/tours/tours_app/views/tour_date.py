from os.path import join

from django.forms import ModelForm
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from tours_app.models import Reservation, Review, Tour, TourDate

__BASE_TEMPLATE_PATH = "tour_dates"


class ReviewModelForm(ModelForm):
    class Meta:
        model = Review
        fields = ["comment", "rating"]


def write_tour_review_view(request: HttpRequest, pk: int) -> HttpResponse:
    if (user := request.user).is_anonymous:
        return redirect("/login")

    try:
        tour = TourDate.objects.get(pk=pk)
    except TourDate.DoesNotExist:
        return Http404("Tour wasn't found")

    form = ReviewModelForm(request.POST or None)
    print(form)
    if request.method == "GET":
        return render(request, join(__BASE_TEMPLATE_PATH, "review.html"), dict(form=form, tour_date=tour))

    if form.is_valid():
        review: Review = form.save(commit=False)
        review.tour_date = tour
        review.traveler = user
        review.save()
        return redirect("/profile")


def all_tours_view(request: HttpRequest) -> HttpResponse:
    return render(request, join(__BASE_TEMPLATE_PATH, "all.html"), dict(tours_dates=TourDate.objects.all()))


def reserve_tour_date_view(request: HttpRequest, pk: int) -> HttpResponse:
    if (user := request.user).is_anonymous:
        return redirect("/login")

    try:
        tour_date = TourDate.objects.get(pk=pk)
    except Tour.DoesNotExist:
        raise Http404("Tour doesn't exist")

    reservation = Reservation(traveler=user, tour_date=tour_date)
    reservation.save()

    return render(request, join(__BASE_TEMPLATE_PATH, "reserved.html"), dict(user=user, tour_date=tour_date))


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

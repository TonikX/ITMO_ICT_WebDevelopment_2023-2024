from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Tour, Reservation
from .forms import ReserveForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from django.db.models import Prefetch


def index(request):
    return render(request, 'index.html')


def tours_by_country_view(request):
    confirmed_reservations = Reservation.objects.filter(is_confirmed=True).select_related('tour')
    tours_with_confirmed_reservations = Tour.objects.prefetch_related(
        Prefetch('reservations', queryset=confirmed_reservations, to_attr='confirmed_reservations')
    ).all()

    tours_by_country = {}
    for tour in tours_with_confirmed_reservations:
        if tour.confirmed_reservations:
            country = tour.country
            if country not in tours_by_country:
                tours_by_country[country] = [tour]
            else:
                tours_by_country[country].append(tour)

    context = {'tours_by_country': dict(sorted(tours_by_country.items()))}
    return render(request, 'tours_by_country.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})


@login_required
def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})


@login_required
def reserve_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.tour = tour
            reservation.save()
            return HttpResponseRedirect(reverse('tour_detail', args=[tour.id]))
    else:
        form = ReserveForm()
    return render(request, 'reserve_tour.html', {'form': form, 'tour': tour})


@login_required
def add_review(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tour = tour
            review.save()
            return HttpResponseRedirect(reverse('tour_detail', args=[tour.id]))
    else:
        form = ReviewForm()
    return render(request, 'tour_comment.html', {'form': form, 'tour': tour})

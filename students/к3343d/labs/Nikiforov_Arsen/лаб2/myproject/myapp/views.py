from django.shortcuts import render, get_object_or_404
from .models import Tour, Agency, Reservation, Review

def tour_list_view(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def tour_detail_view(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'tour_detail.html', {'tour': tour})

def agency_detail_view(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    return render(request, 'agency_detail.html', {'agency': agency})

def reservation_detail_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def review_detail_view(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review_detail.html', {'review': review})

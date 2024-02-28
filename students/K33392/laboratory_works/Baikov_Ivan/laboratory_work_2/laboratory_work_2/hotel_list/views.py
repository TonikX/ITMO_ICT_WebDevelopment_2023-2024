from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Hotel, Reservation, Review
from .forms import ReservationForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    user_has_reservation = False  
    if request.user.is_authenticated:
        user_has_reservation = Reservation.objects.filter(user=request.user, hotel=hotel).exists()
    
    context = {
        'hotel': hotel,
        'user_has_reservation': user_has_reservation,
    }
    
    return render(request, 'hotel_detail.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hotel_list') 
        else:
            pass
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('hotel_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('hotel_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def make_reservation(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.hotel = hotel
            reservation.save()
            return redirect('reservation_confirmation')
    else:
        form = ReservationForm()

    return render(request, 'make_reservation.html', {'form': form, 'hotel': hotel})

@login_required
def reservation_confirmation(request):
    return render(request, 'reservation_confirmation.html')

@login_required
def reservation_list(request):
    user_reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'reservations': user_reservations})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    return render(request, 'cancel_reservation.html', {'reservation': reservation})

def last_month_guests(request):
    one_month_ago = date.today() - timedelta(days=30)
    
    guests = Reservation.objects.filter(check_in_date__gte=one_month_ago)
    
    return render(request, 'last_month_guests.html', {'guests': guests})
    
@login_required
def leave_review(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel

            reservation = Reservation.objects.filter(user=request.user, hotel=hotel).latest('check_in_date')

            review.check_in_date = reservation.check_in_date
            review.check_out_date = reservation.check_out_date

            review.save()
            return redirect('hotel_detail', hotel_id=hotel_id)
    else:
        form = ReviewForm()

    return render(request, 'leave_review.html', {'form': form, 'hotel': hotel})
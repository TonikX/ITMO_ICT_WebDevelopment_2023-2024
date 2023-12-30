from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import datetime
from .forms import *
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated
from django.db.models import Sum, F

@unauthenticated
def registerPage(response):
    if response.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if response.method == 'POST':
            form = CreateUserForm(response.POST) 
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                Customer.objects.create(
                    user=User.objects.get(username=user),
                    name=user,
                    email=form.cleaned_data.get('email'),
                )
                messages.success(response, 'Account was created for ' + user)
                return redirect('login')

    return render(response, 'hotels/register.html', {'form': form})

@unauthenticated
def loginPage(response):
    if response.user.is_authenticated:
        return redirect('profile')
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')

        user = authenticate(response, username=username, password=password)

        if user is not None:
            login(response, user)
            return redirect('home')
        else:
            messages.info(response, 'Username OR password is incorrect')
    context = {}

    return render(response, 'hotels/login.html', context)

def logoutUser(response):
    logout(response)
    return render(response, 'hotels/home.html')

def home(response):
    return render(response, 'hotels/home.html')

def hotels(response):
    hotels = Hotel.objects.all()
    return render(response, 'hotels/hotels.html', {'hotels': hotels})

@login_required(login_url='login')
def profile(response):
    customer = response.user.customer
    bookings = Booking.objects.filter(user=customer)

    context = {'user': response.user, 'bookings': bookings, 'customer': customer}
    return render(response, 'hotels/profile.html', context)

@login_required(login_url='login')
def update_profile(response):
    customer = response.user.customer
    form = CustomerForm(instance=customer)

    if response.method == 'POST':
        form = CustomerForm(response.POST, response.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(response, 'hotels/profile_settings.html', context)

@login_required(login_url='login')
def hotelpage(request, hotel_name):
    hotel = get_object_or_404(Hotel, name=hotel_name)

    rooms = Room.objects.filter(hotel=hotel)
    reviews = Review.objects.filter(booking__room__hotel=hotel)
    last_month = datetime.date.today() - datetime.timedelta(days=30)

    customers_for_last_month = Customer.objects.filter(
        reservations__room__hotel=hotel,
        reservations__check_in_date__gte=last_month,
        reservations__status='Completed'
    ).distinct()

    context = {
        'hotel': hotel,
        'rooms': rooms,
        'reviews': reviews,
        'customers_for_last_month': customers_for_last_month,
    }

    return render(request, 'hotels/hotelpage.html', context)

@login_required(login_url='login')
def booking(request, hotel_name, room_category):
    hotel = get_object_or_404(Hotel, name=hotel_name)
    room = get_object_or_404(Room, hotel=hotel, category=room_category)
    user = request.user.customer

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user.customer
            booking.room = room
            booking.status = 'Pending'
            booking.save()
            return redirect('profile')
    else:

        form = BookingForm(initial={'user':user, 'room': room, 'check_in_date': datetime.date.today(), 'check_out_date': datetime.date.today() + datetime.timedelta(days=1)})

    context = {
        'room': room,
        'form': form,
    }

    return render(request, 'hotels/booking.html', context)

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user.customer)

    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditBookingForm(instance=booking)

    context = {
        'form': form,
        'booking': booking,
    }

    return render(request, 'hotels/edit_booking.html', context)

@login_required(login_url='login')
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user.customer)

    if request.method == 'POST':
        booking.cancel_booking()
        return redirect('profile')

    context = {'booking': booking}
    return render(request, 'hotels/cancel_booking.html', context)

@login_required(login_url='login')
def review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user.customer)
    review = Review.objects.filter(booking=booking).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.user = request.user.customer
            review.save()
            return redirect('profile')
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'booking': booking,
        'review': review,
    }

    return render(request, 'hotels/review.html', context)

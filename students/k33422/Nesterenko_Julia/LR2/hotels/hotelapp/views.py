from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Hotel, Room, Booking, Review
from .forms import GuestCreationForm, BookingCreationForm, ReviewCreationForm


def index(request):
    try:
        h = Hotel.objects.order_by('name')
    except Hotel.DoesNotExist:
        raise Http404("No hotels available")
    data = {'hotel_list': h}
    return render(request, 'index.html', data)


def hotel(request, id):
    try:
        h = Hotel.objects.get(pk=id)
    except Hotel.DoesNotExist:
        raise Http404("Cannot find this hotel")
    try:
        rl = Room.objects.filter(hotel=h)
    except Room.DoesNotExist:
        rl = []
    data = {'hotel': h,
            'room_list': rl,
            'guest_list': h.guests}
    return render(request, 'hotel.html', data)


def room(request, id):
    try:
        r = Room.objects.get(pk=id)
    except Room.DoesNotExist:
        raise Http404("Cannot find this room")
    if request.method == 'POST':
        u = request.user
        d_f = request.POST.get('from')
        d_u = request.POST.get('until')
        if d_f > d_u:
            messages.info(request, 'Departure should be later than Arrival')
        elif not r.available(d_f, d_u):
            messages.info(request, 'Room is booked for these days')
        else:
            post_data = {'guest': u, 'room': r, 'date_from': d_f, 'date_until': d_u, 'status': 'Awaits'}
            f = BookingCreationForm(post_data)
            f.save()
            return redirect('/account')

    data = {'room': r}
    return render(request, 'room.html', data)


@login_required(login_url='login')
def cancelbooking(request, id):
    try:
        b = Booking.objects.get(pk=id)
    except Booking.DoesNotExist:
        raise Http404("Cannot find this booking")
    if b.guest != request.user:
        raise HttpResponseNotAllowed("Only user who made the booking can cancel it")
    b.status = 'Canceled'
    b.save(update_fields=['status'])
    return redirect('/account')


@login_required(login_url='login')
def review(request, booking_id):
    try:
        b = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        raise Http404("Cannot find this booking")
    if b.guest != request.user:
        raise HttpResponseNotAllowed("Only user who made the booking can review it")
    r = request.POST.get('rating')
    bod = request.POST.get('body')
    post_data = {'booking': b, 'rating': r, 'body': bod}
    f = ReviewCreationForm(post_data)
    f.save()
    return redirect('/account')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    f = GuestCreationForm()

    if request.method == 'POST':
        f = GuestCreationForm(request.POST, request.FILES)
        try:
            f.save()
            return redirect('login')
        except ValueError:
            for err in dict(f.errors).values():
                messages.info(request, err)

    data = {'form': f}
    return render(request, 'register.html', data)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        Guest = get_user_model()
        try:
            user = Guest.objects.get(username=u)
            if check_password(p, user.password) or p == user.password:
                login(request, user)
                return redirect('/', user)
            else:
                messages.info(request, 'Incorrect password')
        except Guest.DoesNotExist:
            messages.info(request, 'Incorrect username')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def account(request):
    u = request.user
    data = {'user': u}
    return render(request, 'account.html', data)

from datetime import datetime, timedelta, date

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, Booking, Room, Guest, Feedback
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import FeedbackForm, BookingForm


def main(request):
    return render(request, 'main.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'main.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user_book(request, guest_passport):
    print("guest", guest_passport)
    guest = Guest.objects.filter(passport=guest_passport).get()
    print(guest)
    need_book = Booking.objects.filter(guest=guest)
    print(need_book)
    current_book = {"object_list": need_book}
    return render(request, 'user_bookings.html', current_book)

@login_required
def new_book(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        try:
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                passport = booking_form.cleaned_data['passport']
            if not Guest.objects.filter(passport=passport).exists():
                Guest.objects.create(
                    user_id=request.user.id,
                    first_name=booking_form.cleaned_data['first_name'],
                    last_name=booking_form.cleaned_data['last_name'],
                    passport=passport)

            tuple1 = booking_form.cleaned_data['check_in_date']
            tuple2 = booking_form.cleaned_data['check_out_date']
            check_in_date = date(tuple1.year, tuple1.month, tuple1.day)
            check_out_date = date(tuple2.year, tuple2.month, tuple2.day)
            duration = (check_out_date - check_in_date).days
            new_booking = Booking(
                room=room,
                hotel=room.hotel,
                guest=Guest.objects.filter(passport=passport).get(),
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                price=duration * room.cost
            )
            Booking.save(new_booking)
            return redirect(request, "user_book", guest_passport=passport)
        except:
            return render(request, 'new_book.html')
    else:
        booking_form = BookingForm()
    return render(request, 'new_book.html', {'form': booking_form})


@login_required
def my_bookings(request):
    if request.method == 'POST':
        passport = request.POST.get('passport_user')

        print(Guest.objects.filter(passport=passport))
        print('redirect')
        # args = {'guest_passport': passport}
        return redirect("user_book", guest_passport=passport)
        # return user_book(request, passport)
    else:
        return render(request, "my_bookings.html")



@login_required
class UpdateBooking(UpdateView):
    model = Booking
    fields = ['check_in_date', 'check_out_date']
    template_name = 'update_book.html'
    success_url = '/my_bookings/'


@login_required
class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_book.html'
    success_url = '/my_bookings/'

@login_required
def new_feedback(request, pk):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        print(feedback_form)
        booking = Booking.objects.filter(id=pk).get()
        print(booking)
        Feedback.objects.create(booking=booking,
                                check_in_date=booking.check_in_date,
                                check_out_date=booking.check_out_date,
                                text=feedback_form.cleaned_data['text'],
                                rate=feedback_form.cleaned_data['rate'],
                                author=request.user.username)
        return redirect("feedback_list")
    else:
        feedback_form = FeedbackForm()
        return render(request, 'new_feedback.html', {'form': feedback_form})

@login_required
def all_feedbacks(request):
    feedbacks = {"object_list": Feedback.objects.all()}
    print(feedbacks)
    return render(request, 'all_feedbacks.html', feedbacks)

@login_required
def hotel_guests(request, hotel_id):
    one_month_ago = datetime.now()
    # one_month_ago = datetime.now() - timedelta(days=30)
    list_of_guests = Booking.objects.filter(hotel=hotel_id, check_in_date__gte=one_month_ago)

    print(list_of_guests)
    hotel_name = Hotel.objects.filter(id=hotel_id).get().name

    list_of_guests = {
        "list_of_guests": list_of_guests,
        "hotel_name": hotel_name}
    return render(request, 'hotel_guests.html', list_of_guests)

@login_required
def hotel_rooms(request, hotel_id):
    rooms_in_hotel = Room.objects.filter(hotel=hotel_id)
    hotel_name = Hotel.objects.filter(id=hotel_id)
    list_of_rooms = {
        "object_list": rooms_in_hotel,
        "hotel_name": hotel_name}
    return render(request, 'hotel_rooms.html', list_of_rooms)

@login_required
class HotelList(ListView):
    model = Hotel
    template_name = 'hotel_list.html'

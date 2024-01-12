
from django.shortcuts import render, redirect
from hotel_app.models import Hotel, Room, Booking, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, BookRoomForm, ReviewForm


def leave_review(request, *args, **kwargs):
    model = Room
    queryset = model.objects.all()
    hotel = kwargs['hotel_city']
    queryset = queryset.filter(hotel__city=hotel)
    room_type = kwargs['room_type']
    room = queryset.get(type=room_type)
    if request.POST:
        form = ReviewForm(request.POST, user=request.user, room=room)
        if form.is_valid():
            comment = form.save()
            return redirect("/booking/")
    form = ReviewForm()
    return render(request=request, template_name="review.html", context={"review_form": form})


def booking_view(request, *args, **kwargs):
    model = Room
    queryset = model.objects.all()
    hotel = kwargs['hotel_city']
    queryset = queryset.filter(hotel__city=hotel)
    room_type = kwargs['room_type']
    room = queryset.get(type=room_type)

    comm_model = Comment
    comm_queryset = comm_model.objects.all()
    comments = comm_queryset.filter(room=room)
    print(room)
    if request.POST:
        form = BookRoomForm(request.POST, user=request.user, room=room)
        if form.is_valid():
            booking = form.save()
            return redirect("/booking/")
    form = BookRoomForm()
    return render(request=request, template_name="room_detail.html", context={"booking_form": form,
                                                                              "comments": comments})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


class BookingListView(ListView):
    model = Booking
    queryset = model.objects.all()

    def get_queryset(self):
        try:
            queryset = self.queryset.filter(user=self.request.user)

        except ValueError:
            queryset = self.model.objects.none()

        return queryset


class HotelRetrieveView(DetailView):
    model = Hotel


class HotelListView(ListView):
    model = Hotel


class RoomListView(ListView):
    model = Room
    queryset = model.objects.all()


    def get_queryset(self):
        hotel = self.kwargs['hotel_city']

        if hotel:

            try:
                queryset = self.queryset.filter(hotel__city=hotel)

            except ValueError:
                queryset = self.model.objects.none()
            return queryset

        return self.queryset


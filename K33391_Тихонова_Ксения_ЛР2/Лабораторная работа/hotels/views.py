import datetime
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from .forms import ReservationForm, RegistrationForm, LoginForm, CommentForm
from .models import TypeOfRoom, Room, Reservation, Hotel, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404



def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("user_login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)

        username = user_form.data.get("username")
        password = user_form.data.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect("user_login")

        login(request, user)
        return redirect("hotel_list")
    else:
        user_form = LoginForm()

    return render(request, "login.html", {"user_form": user_form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


def hotel_list(request):

    if request.method != "GET":
        return Http404(f"Method {request.method} not supported")

    capacity = request.GET.get("capacity", None)
    available_capacities = TypeOfRoom.objects.values_list('capacity', flat=True)

    hotels = Hotel.objects.all()

    if capacity is not None:
        hotels = hotels.filter(rooms__type__capacity__gte=capacity)

    return render(
        request,
        "list.html",
        {
            "capacity": capacity,
            "available_capacities": available_capacities,
            "hotels": hotels
        },
    )


def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    if request.method != "GET":
        return redirect("hotel_detail", hotel_id)
    else:
        rooms_set = Room.objects.filter(hotel__id=hotel_id).order_by("number")
        rooms = []

        for room in rooms_set:
            if not Reservation.objects.filter(
                    room=room,
                    date_start__lte=datetime.date.today(),
                    date_finish__gte=datetime.date.today()
            ).exists():
                rooms.append({
                    "name": f"{room.number}",
                    "capacity": f"{room.type.capacity}",
                    "conveniences": f"{room.type.conveniences}",
                    "cost": f"{room.type.cost}"
                })

        user_has_reservation = Reservation.objects.filter(
            passenger=request.user,
            room__hotel=hotel,
            date_start__lte=datetime.date.today(),
            date_finish__gte=datetime.date.today()
        ).exists()

        reservation_form = ReservationForm(hotel)
        comments = Comment.objects.filter(hotel=hotel)

        comment_form = CommentForm()

        return render(
            request,
            "detail.html",
            {
                "hotel": hotel,
                "comments": comments,
                "comments_exists": bool(comments.count()),
                "rooms": rooms,
                "form": reservation_form,
                "user": request.user,
                "comment_form": comment_form,
                "user_has_reservation": user_has_reservation
            },
        )

@login_required(login_url='/login/')
def reserve_room(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    if request.method != "GET":
        room = Room.objects.filter(number=request.POST['room']).first()
        try:
            date_start = datetime.datetime.strptime(request.POST["date-start"], "%d.%m.%Y")
            date_finish = datetime.datetime.strptime(request.POST["date-finish"], "%d.%m.%Y")

            form = ReservationForm({"room": room, "date_start": date_start, "date_finish": date_finish})

            if not form.is_valid():
                return redirect("hotel_detail", hotel_id)

            reservation = form.save(commit=False)
            reservation.passenger = request.user
            reservation.room = room
            reservation.save()

        except Exception:
            return render(request, "reserve_room.html", {'form' : ReservationForm(), "hotel": hotel, "warning": True})

        return redirect("hotel_detail", hotel_id)

    else:
        return render(request, "reserve_room.html", {'form' : ReservationForm(), "hotel": hotel, "warning": False})


@login_required(login_url='/login/')
def leave_comment(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if Reservation.objects.filter(passenger=request.user, room__hotel=hotel_id).exists():
                comment = comment_form.save(commit=False)
                comment.hotel = Hotel.objects.get(id=hotel_id)
                comment.author = request.user
                comment.save()
        return redirect("hotel_detail/", hotel_id)
    else:
        return render(request, "leave_comment.html", {"comment_form": CommentForm(), "hotel": hotel})

# @login_required(login_url='/login/')
def reservations_for_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    reservations = Reservation.objects.filter(passenger=request.user)
    return render(request, "reservation_for_user.html", {"reservations": reservations})


def reservation_update(request, reservation_id):

    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        form = ReservationForm(data=request.POST, instance=reservation)
        if not form.is_valid():
            return redirect("reservation_update", reservation_id)

        form.save()
        return redirect("hotel_detail", reservation.room.hotel.id)
    else:
        form = ReservationForm(instance=reservation)
        return render(
            request,
            "reservation_update.html",
            {"form": form, "reservation": reservation},
        )


@login_required(login_url='/login/')
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, passenger=request.user)

    if request.method == "POST":
        reservation.delete()
        return redirect("hotel_detail", reservation.room.hotel.id)
    else:
        return render(
            request,
            "reservation_delete.html",
            {"reservation": reservation},
        )

def list_passengers(request, hotel_id):
    hotel = Hotel.objects.filter(id=hotel_id).first() 
    reservations = Reservation.objects.filter(room__hotel=hotel.id)
    # reservations = Reservation.objects.filter(room__hotel=hotel_id, date_start__gt = datetime.date.today()-datetime.timedelta(days=30)) 

    return render(request, "list_users.html", {"is_admin": request.user.is_superuser, "reservations": reservations})

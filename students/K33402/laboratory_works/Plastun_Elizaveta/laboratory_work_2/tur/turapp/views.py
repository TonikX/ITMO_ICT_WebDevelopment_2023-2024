from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()

    return render(request, "register.html", {"user_form": user_form})


def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def admin_check(user):
    return user.groups.filter(name='Администратор').exists()


def index(request):
    user_is_admin = request.user.groups.filter(name='Администратор').exists()
    context = {"dataset": Tour.objects.all(), 'user_is_admin': user_is_admin}
    return render(request, 'index.html', context)


def my_tours(request):
    if not request.user.is_authenticated:
        return redirect('login/')

    user_id = request.user.id
    is_editor = request.user.groups.filter(name='Администратор').exists()

    if is_editor:
        user_reservations = Reservation.objects.all()
        context = {"dataset": user_reservations}
        return render(request, 'all_tours.html', context)
    else:
        user_reservations = Reservation.objects.filter(user=user_id)
        context = {"dataset": user_reservations}
        return render(request, 'my_tours.html', context)


def tour_page(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    comments = TourComment.objects.filter(tour=tour)

    if request.user.is_authenticated:
        user_reservation = Reservation.objects.filter(tour=tour, user=request.user)
    else:
        user_reservation = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tour = tour
            comment.user = request.user
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'tour_page.html',
                  {'tour': tour, 'form': form, 'comments': comments, 'user_reservation': user_reservation, })


def user_logout(request):
    logout(request)
    return redirect("login")


def delete_comment(request, comment_id):
    comment = get_object_or_404(TourComment, id=comment_id)

    if comment.user == request.user:
        comment.delete()

    return redirect('tour_page', tour_id=comment.tour.id)


def create_reservation(request, tour_id):
    context = {}
    tour = get_object_or_404(Tour, id=tour_id)
    user = request.user

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.tour = tour
            reservation.user = user
            reservation.status = 'Ожидает подтверждения'
            reservation.save()
            return redirect('tour_page', tour_id=tour_id)
    else:
        form = ReservationForm()

    context['form'] = form
    return render(request, "create_reservation.html", context)


def delete_reservation(request, tour_id):
    if request.method == 'POST':
        tour = get_object_or_404(Tour, id=tour_id)
        user = request.user

        try:
            reservation = Reservation.objects.get(tour=tour, user=user)
            reservation.delete()
        except Reservation.DoesNotExist:
            pass

    return redirect('tour_page', tour_id=tour_id)


@login_required
@user_passes_test(admin_check)
def delete_reservation_admin(request, reservation_id):
    if request.method == 'POST':
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            reservation.delete()
        except Reservation.DoesNotExist:
            pass

    return redirect('my_tours')


@login_required
@user_passes_test(admin_check)
def access_reservation_admin(request, reservation_id):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id)
        reservation.status = 'Подтвержден'
        reservation.save()

    return redirect('my_tours')


@login_required
@user_passes_test(admin_check)
def cancel_reservation_admin(request, reservation_id):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id)
        reservation.status = 'Ожидает подтверждения'
        reservation.save()

    return redirect('my_tours')


@login_required
@user_passes_test(admin_check)
def create_tour(request):
    context = {}
    form = TourForm()

    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context['form'] = form
    return render(request, "create_tour.html", context)


@login_required
@user_passes_test(admin_check)
def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == 'POST':
        tour.delete()
        return redirect('index')

    return render(request, 'delete_tour.html', {'tour': tour})

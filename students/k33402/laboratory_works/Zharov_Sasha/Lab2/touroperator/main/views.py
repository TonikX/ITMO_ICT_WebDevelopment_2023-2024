from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, TourComment, Reservation
from .forms import CommentForm, ReservationForm, TourForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def admin_check(user):
    return user.groups.filter(name='Администратор').exists()

def index(request):
    user_is_admin = request.user.groups.filter(name='Администратор').exists()
    context = {"dataset": Tour.objects.all(), 'user_is_admin': user_is_admin}
    return render(request, 'main/index.html', context)

def my_tours(request):

    if not request.user.is_authenticated:
        return redirect('/users/login/')
    
    user_id = request.user.id
    is_editor = request.user.groups.filter(name='Администратор').exists()

    if is_editor: 
        user_reservations = Reservation.objects.all()
        context = {"dataset": user_reservations}
        return render(request, 'main/all_tours.html', context)
    else:
        user_reservations = Reservation.objects.filter(user=user_id)
        context = {"dataset": user_reservations}
        return render(request, 'main/my_tours.html', context)

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


    return render(request, 'main/tour_page.html', {'tour': tour, 'form': form, 'comments': comments, 'user_reservation': user_reservation,})

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
    return render(request, "main/create_reservation.html", context)

def delete_reservation(request, tour_id):
    if request.method == 'POST':
        tour = get_object_or_404(Tour, id=tour_id)
        user = request.user

        try:
            reservation = Reservation.objects.get(tour=tour, user=user)
            print(reservation)
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
    return render(request, "main/create_tour.html", context)

@login_required
@user_passes_test(admin_check)
def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    
    if request.method == 'POST':
        tour.delete()
        return redirect('index')
    
    return render(request, 'main/delete_tour.html', {'tour': tour})
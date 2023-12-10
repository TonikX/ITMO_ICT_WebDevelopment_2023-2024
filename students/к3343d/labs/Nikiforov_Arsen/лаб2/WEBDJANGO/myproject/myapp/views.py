from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .models import Tour, Reservation, Review, SoldTour, TourReservation
from .forms import ReservationForm, ReviewForm, SoldTourForm, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string

def add_review(request, tour_id=None):
    if request.method == 'POST':
        if tour_id is not None:
            tour = get_object_or_404(Tour, pk=tour_id)
            review_text = request.POST.get('review_text', '')
            review = Review.objects.create(tour=tour, user=request.user, text=review_text)

            reviews_html = render_to_string('reviews.html', {'reviews': tour.review_set.all()})

            return render(request, 'reviews.html', {'reviews': tour.review_set.all()})
        else:
            return render(request, 'reviews.html', {'reviews': []})
    else:
        return render(request, 'reviews.html', {'reviews': []})


def menu(request):
    return render(request, 'menu.html')



def home(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        elif 'login' in request.POST:
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect('tour_list')
    else:
        form = UserCreationForm() if 'register' in request.GET else AuthenticationForm()

    tours = Tour.objects.all()  
    form_name = 'register' if isinstance(form, UserCreationForm) else 'login'
    return render(request, 'home.html', {'form': form, 'tours': tours, 'form_name': form_name})





def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('user_login')  
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



@login_required
def buy_tour(request, tour_id):
    if request.method == 'POST':
        # Обработка POST-запроса для покупки тура
        tour = Tour.objects.get(id=tour_id)
        user = request.user

        
        price = tour.price  

        SoldTour.objects.create(tour=tour, buyer=user, price=price)

        # После успешной покупки редиректите пользователя на страницу с турами или другую страницу
        return redirect('tour_list')




def tour_list(request):
    tours = Tour.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tour = Tour.objects.get(id=request.POST.get('tour_id'))
            review.save()
            return redirect('tour_list')
    else:
        form = ReviewForm()

    return render(request, 'tour_list.html', {'tours': tours, 'form': form})



def reserve_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.tour = tour
            reservation.save()
            messages.success(request, 'Tour reserved successfully!')
            return redirect('tour_list')
    else:
        form = ReservationForm()

    return render(request, 'myapp/reserve_tour.html', {'form': form, 'tour': tour})




def buy_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)

    if request.method == 'POST':
        form = SoldTourForm(request.POST)
        if form.is_valid():
            sold_tour = form.save(commit=False)
            sold_tour.buyer = request.user
            sold_tour.tour = tour
            # Устанавливаем фиксированное значение цены, например, 100.00
            sold_tour.price = 100.00
            sold_tour.save()

            # Помечаем тур как проданный
            tour.is_sold = True
            tour.save()

            messages.success(request, 'Tour purchased successfully!')
            return redirect('tour_list')
    else:
        form = SoldTourForm()

    return render(request, 'myapp/buy_tour.html', {'form': form, 'tour': tour})




def sell_tour(request, tour_id):
    if request.method == 'POST':
        form = SoldTourForm(request.POST)
        if form.is_valid():
            sold_tour = form.save(commit=False)
            sold_tour.user = request.user
            sold_tour.tour_id = tour_id
            sold_tour.save()
            return redirect('sold_tours')  # Перенаправить на страницу с проданными турами
    else:
        form = SoldTourForm()

    return render(request, 'sell_tour.html', {'form': form})






def sold_tours(request):
    sold_tours = SoldTour.objects.filter(buyer=request.user)
    return render(request, 'myapp/sold_tours.html', {'sold_tours': sold_tours})





def tour_detail(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    reviews = Review.objects.filter(tour=tour)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('tour_detail', tour_id=tour_id)
    else:
        form = ReviewForm()

    context = {
        'tour': tour,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'myapp/tour_detail.html', context)





def reserve_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.tour = tour
            reservation.user = request.user
            reservation.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm()

    return render(request, 'myapp/reserve_tour.html', {'form': form, 'tour': tour})




def user_reservations(request):
    user = request.user
    reservations = TourReservation.objects.filter(user=user)
    return render(request, 'user_reservations.html', {'reservations': reservations})



def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'edit_reservation.html', {'form': form, 'reservation': reservation})


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    if request.method == 'POST':
        reservation.delete()
        return redirect('user_reservations')

    return render(request, 'delete_reservation.html', {'reservation': reservation})


def confirm_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.is_confirmed = True
    reservation.save()
    return redirect('tour_list')

def reject_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('tour_list')




def reserve_tour(request, tour_id):
    if request.method == 'POST':
        tour = Tour.objects.get(pk=tour_id)
        reservation = Reservation(tour=tour, user=request.user)
        reservation.save()
        return redirect('tour_list')

    tour = Tour.objects.get(pk=tour_id)
    return render(request, 'reserve_tour.html', {'tour': tour})









# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return redirect('login')  
#     else:
#         form = RegistrationForm()

#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def reserve_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.tour = tour
            reservation.save()
            messages.success(request, 'Tour reserved successfully!')
            return redirect('tour_list')
    else:
        form = ReservationForm()

    return render(request, 'reserve_tour.html', {'form': form, 'tour': tour})

@login_required
def review_tour(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tour = tour
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('tour_list')
    else:
        form = ReviewForm()

    return render(request, 'review_tour.html', {'form': form, 'tour': tour})

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'user_reservations.html', {'reservations': reservations})

from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            guest = form.save(commit=False)

            guest.profile_picture = form.cleaned_data['profile_picture']

            guest.save()
            return redirect('/auth/login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/auth/login')


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile/profile.html', {'user': user})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Guest deleted successfully!')
        return redirect('/auth/login')
    return render(request, 'profile/delete_profile.html')


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        guest = form.save(commit=False)

        guest.profile_picture = form.cleaned_data['profile_picture']

        guest.save()
        messages.success(request, 'Guest updated successfully!')
        return redirect('/profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'profile/edit_profile.html', {'form': form})


def show_user(request, user_id):
    try:
        guest = Guest.objects.get(pk=user_id)  
    except Room.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user/user.html', {'guest': guest})


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'profile/reservations.html'
    context_object_name = 'reservations'


class ReservationDisplay(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'profile/reservation_detail.html'
    context_object_name = 'res'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context


class ReservationComment(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Reservation
    form_class = ReviewForm
    template_name = 'profile/reservation_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ReservationComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('Reservation_detail', kwargs={'pk': post.pk}) + '#comments'


class ReservationDetailView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = ReservationDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReservationComment.as_view()
        return view(request, *args, **kwargs)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'body']
    template_name = 'profile/review_update.html'

    def get_success_url(self) -> str:
        review = self.get_object()
        return reverse('Reservation_detail', kwargs={'pk': review.reservation.pk})


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'profile/review_delete.html'

    def get_success_url(self) -> str:
        review = self.get_object()
        return reverse('Reservation_detail', kwargs={'pk': review.reservation.pk})
    

def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'main/rooms_list.html', {'rooms': rooms})


def show_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)  
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'main/room.html', {'room': room})


def list_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'main/hotels_list.html', {'hotels': hotels})


def show_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)  
    except Room.DoesNotExist:
        raise Http404("Hotel does not exist")
    return render(request, 'main/hotel.html', {'hotel': hotel})


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/reservation_edit.html'
    context_object_name = 'res'
    success_url = reverse_lazy('Show_reservations')


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservations/reservation_delete.html'
    success_url = reverse_lazy('Show_reservations')


class ReservationCreate(LoginRequiredMixin, ListView):    
    template_path = 'reservations/reservation_create.html'
    form_class = ReservationForm
    success_url = reverse_lazy('Show_reservations')

    def get(self, request, room_id, *args, **kwargs):
        form = self.form_class()        
        form.guest = request.user
        form.room = Room.objects.get(pk=room_id)    
        context = {'form': form}
        return render(request, self.template_path, context)
    
    def post(self, request, room_id, *args, **kwargs):        
        form = self.form_class(request.POST)
        form.instance.guest = request.user
        form.instance.room = Room.objects.get(pk=room_id)   
        if form.is_valid():
            form.instance.guest = request.user     
            form.instance.room = Room.objects.get(pk=room_id)         
            form.save()
            messages.success(request, 'Your reservation was successfully made!')     
            return redirect(self.success_url) 
        else:
            messages.error(request, 'Error: Invalid form data. Please try again.')
            return render(request, 'reservations/reservation_unavailable.html', {'room_id': room_id})
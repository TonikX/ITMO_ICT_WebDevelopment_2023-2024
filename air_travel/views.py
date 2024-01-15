from datetime import datetime, timezone

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView

from air_travel.forms import NewPassengerForm, CommentFlightForm
from air_travel.models import Booking, Flight, Comments


class Main(View):
    def get(self, request):
        flights = Flight.objects.all()
        return render(request, 'main.html', context=locals())


class RegisterPassenger(View):
    def get(self, request):
        form = NewPassengerForm()
        return render(request, 'register.html', context=locals())

    def post(self, request):
        form = NewPassengerForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        return render(request, 'register.html', context=locals())


class AuthUser(LoginView):
    template_name = 'login.html'
    next_page = 'profile'


class LogOut(LogoutView):
    next_page = 'main_page'


class UserProfile(View):
    def get(self, request):
        booking = Booking.objects.filter(user_id=request.user.id)
        return render(request, 'profile.html', context=locals())


class EditBooking(UpdateView):
    model = Booking
    fields = ['flight']
    template_name = 'editBooking.html'
    success_url = reverse_lazy('profile')


class DeleteBooking(DeleteView):
    model = Booking
    success_url = reverse_lazy('profile')
    template_name = 'delete_booking.html'


class DetailFlight(DetailView):
    model = Flight
    template_name = 'detailFlight.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight'] = Flight.objects.get(id=self.object.id)
        context['user_comments'] = Comments.objects.filter(booking_id=Booking.objects.filter(flight_id=self.object.id)[0].id)
        context['form'] = CommentFlightForm()
        return context

    def post(self, request, pk):
        form = CommentFlightForm(request.POST)
        fly = Flight.objects.get(id=pk)
        if datetime.now().replace(tzinfo=timezone.utc) > fly.date_arrivals.replace(tzinfo=timezone.utc):
            if form.is_valid():
                comment = form.save(commit=False)
                comment.booking = Booking.objects.filter(flight_id=pk)[0]
                form.save()
        return redirect('main_page')

class DetailFlightForBooking(DetailView):
    model = Flight
    template_name = 'detail_flight_for_booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight'] = Flight.objects.get(id=self.object.id)
        bookings = Booking.objects.filter(flight_id=self.object.id)
        context['passengers'] = list(bookings)
        return context

    def post(self, request, pk):
        book = Booking.objects.filter(flight_id=pk).filter(user=request.user)
        fly = Flight.objects.get(id=pk)
        if not book:
            if datetime.now().replace(tzinfo=timezone.utc) < fly.date_arrivals.replace(tzinfo=timezone.utc):
                book = Booking.objects.create(flight_id=pk, user=request.user)
                book.save()
                return redirect('profile')
        return render(request, 'exception_booking.html', locals())

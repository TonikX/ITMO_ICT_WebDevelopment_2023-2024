from datetime import datetime

from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .forms import SignUpForm, TicketForm, CommentForm
from .models import Flight, Plane, Seat, Traveler, Ticket, Comment
from django.views import generic



def HomeSortView(request):
    flights = Flight.objects.filter(departure_time__date__gt=datetime.now().date())
    return render(request, 'home.html', {'object_list': flights})


#class TicketTableView(ListView):
#    model = Ticket
#    template_name = 'ticket_table.html'


def TicketFlightTableView(request, flight_id):
    tickets = Ticket.objects.filter(flight_id=flight_id)
    return render(request, 'ticket_table.html', {'tickets': tickets})


class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight_detail.html'


def UserWithFlightsView(request, user_id):
    tickets = Ticket.objects.filter(traveler_id=user_id)
    tick = []
    for i in range(len(tickets)):
        tick.append(tickets[i].flight_id.pk)
    flights = Flight.objects.filter(pk__in=tick)
    flights_1 = flights.filter(departure_time__date__gt=datetime.now().date())
    flights_2 = flights.filter(departure_time__date__lte=datetime.now().date())
    user = get_object_or_404(Traveler, pk=user_id)
    return render(request, 'user_page.html', {'tickets': tickets, 'flights_1': flights_1, 'flights_2': flights_2, 'user': user})


def SeatsView(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    tickets = Ticket.objects.filter(flight_id=flight_id)
    tick = []
    for i in range(len(tickets)):
        tick.append(tickets[i].seat_id.name)
    seats = Seat.objects.filter(plane_id=flight.plane_id)
    seats = seats.exclude(pk__in=tick)
    user_ticket = tickets.filter(traveler_id=request.user.pk)
    return render(request, 'seats.html', {'seats': seats, 'flight': flight, 'tickets': user_ticket})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class TicketBookNewView(generic.CreateView):
    model = Ticket
    template_name = 'booking.html'
    form_class = TicketForm

    def get_success_url(self):
        return reverse('user-page', kwargs={'user_id': self.request.user.pk})

    def form_valid(self, form):
        form.instance.traveler_id = self.request.user
        form.instance.flight_id = Flight.objects.get(pk=self.kwargs['flight_id'])
        form.instance.seat_id = Seat.objects.get(pk=self.kwargs['seat_id'])
        return super().form_valid(form)


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'delete_booking.html'

    def get_success_url(self):
        return reverse('user-page', kwargs={'user_id': self.request.user.pk})


class TicketUpdateView(UpdateView):
    model = Ticket
    template_name = 'update_booking.html'
    form_class = TicketForm

    def get_success_url(self):
        return reverse('user-page', kwargs={'user_id': self.request.user.pk})

    def form_valid(self, form):
        form.instance.traveler_id = self.request.user
        form.instance.flight_id = Flight.objects.get(pk=Ticket.objects.get(pk=self.kwargs['pk']).flight_id.pk)
        form.instance.seat_id = Seat.objects.get(pk=Ticket.objects.get(pk=self.kwargs['pk']).seat_id.pk)
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('flight-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.flight = Flight.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.date_flight = Flight.objects.get(pk=self.kwargs['pk']).departure_time
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from . import models
from .mixins import UserReviewMixin


class IndexRedirectView(RedirectView):
    url = reverse_lazy('flights')


class FlightListView(ListView):
    model = models.Flight
    template_name = 'flights/flight_list.html'


class FlightDetailView(DetailView):
    model = models.Flight
    template_name = 'flights/flight_detail.html'


class FlightSeatsDetailView(DetailView):
    model = models.Flight
    template_name = 'flights/flight_seats.html'
    context_object_name = 'flight'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flight = self.object
        tickets = models.Ticket.objects.filter(flight=flight).order_by('seat_class', 'seat')
        context['tickets'] = tickets
        return context


class TicketBookView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        ticket_id = kwargs.get('pk')
        ticket = get_object_or_404(models.Ticket, pk=ticket_id)
        flight = ticket.flight
        
        existing_reservation = models.Reservation.objects.filter(user=request.user, ticket__flight=flight).first()
        
        if flight.status != 'scheduled':
            raise PermissionDenied("Бронирование доступно только для запланированных рейсов.")
        
        if existing_reservation and existing_reservation.ticket != ticket:
            existing_ticket = existing_reservation.ticket
            existing_ticket.is_booked = False
            existing_ticket.save()
            existing_reservation.delete()
        
        if not ticket.is_booked:
            ticket.is_booked = True
            ticket.save()
            models.Reservation.objects.update_or_create(user=request.user, ticket=ticket)
        
        return redirect('home')


class ReservationListView(LoginRequiredMixin, ListView):
    model = models.Reservation
    template_name = 'reservation_list.html'

    def get_queryset(self):
        return models.Reservation.objects.filter(user=self.request.user)


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Reservation
    success_url = reverse_lazy('home')
    context_object_name = 'reservation'

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        ticket = self.object.ticket
        ticket.is_booked = False
        ticket.save()
    
        response = super().delete(request, *args, **kwargs)
    
        return response


class ReviewListView(LoginRequiredMixin, ListView):
    model = models.Review
    template_name = 'flights/reviews_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight_id'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        return models.Review.objects.filter(flight_id=self.kwargs['pk']).select_related('user', 'flight')


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.Review
    fields = ['comment', 'rating']
    template_name = 'flights/review_create.html'
    
    def get_success_url(self):
        return reverse('reviews-list', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flight_id'] = self.kwargs['pk']
        return context

    def dispatch(self, request, *args, **kwargs):
        flight = get_object_or_404(models.Flight, pk=self.kwargs['pk'])

        has_reservation = models.Reservation.objects.filter(user=self.request.user, ticket__flight=flight).exists()
        if not has_reservation or flight.status != 'completed':
            raise PermissionDenied("Вы не имеете права на это действие.")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        flight = get_object_or_404(models.Flight, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.flight = flight
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UserReviewMixin, UpdateView):
    model = models.Review
    fields = ['comment', 'rating']
    template_name = 'flights/review_update.html'

    def get_success_url(self):
        return reverse('reviews-list', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = self.get_object()
        context['flight_id'] = review.flight_id
        return context


class ReviewDeleteView(LoginRequiredMixin, UserReviewMixin, DeleteView):
    model = models.Review
    
    def get_success_url(self):
        return reverse('reviews-list', args=[self.kwargs['pk']])

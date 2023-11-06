from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, DetailView, \
    UpdateView

from .models import Hotel, Reservation
from .forms import VisitorCreationForm


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hotels'


class UserRegistrationView(CreateView):
    form_class = VisitorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ReservationEditView(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = ['room_type', 'start_date', 'end_date']
    template_name = 'reservation_form.html'
    success_url = reverse_lazy('reservations_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_confirm_delete.html'
    success_url = reverse_lazy('reservations_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)



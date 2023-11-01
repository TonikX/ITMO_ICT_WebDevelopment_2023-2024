from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reservation, Tour
from django.http import HttpResponseBadRequest


class ReservationCreationView(LoginRequiredMixin, CreateView):
    model = Reservation
    success_url = "/tours"
    fields = ['start_date', 'end_date']
    template_name = "reservation_form.html"

    def form_valid(self, form):
        tour_id = self.kwargs['id']
        if not tour_id:
            return HttpResponseBadRequest("Invalid tour id")

        tour_id = int(tour_id)
        reservation: Reservation = form.instance
        reservation.tourist = self.request.user
        reservation.tour = Tour.objects.get(pk=tour_id)
        return super().form_valid(form)


class ToursListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = "tour_list.html"



class TourDetailView(LoginRequiredMixin, DetailView):
    model = Tour
    template_name = "tour_detail.html"

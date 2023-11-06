from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Reservation, Tour, Review
from django.http import HttpResponseBadRequest


class ReservationCreationView(LoginRequiredMixin, CreateView):
    model = Reservation
    success_url = "/reservations"
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


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    success_url = "/reservations"
    fields = ["start_date", "end_date"]
    template_name = "reservation_form.html"

    def form_valid(self, form):
        reservation_id = self.kwargs['pk']
        if not reservation_id:
            return HttpResponseBadRequest("Invalid reservation id")

        reservation_id = int(reservation_id)
        prev_reservation: Reservation = Reservation.objects.get(pk=reservation_id)
        if prev_reservation.tourist != self.request.user:
            return HttpResponseBadRequest("Invalid reservation id")

        reservation: Reservation = form.instance
        reservation.tourist = self.request.user
        reservation.tour = prev_reservation.tour
        return super().form_valid(form)


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "reservation_list.html"
    queryset = Reservation.objects.all()

    def get_queryset(self):
        user = self.request.user
        query_set = self.queryset.filter(tourist=user)

        return query_set


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = "reservation_detail.html"


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    success_url = "/reservations"
    template_name = "reservation_delete.html"

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ReservationDeleteView, self).form_valid(form)


class ToursListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = "tour_list.html"


class TourDetailView(LoginRequiredMixin, DetailView):
    model = Tour
    template_name = "tour_detail.html"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    success_url = "/reservations"
    template_name = "review_form.html"
    fields = ['rating', 'comment']

    def form_valid(self, form):
        reservation_id = self.kwargs['id']
        if not reservation_id:
            return HttpResponseBadRequest("Invalid tour id")

        reservation_id = int(reservation_id)
        review: Review = form.instance
        review.reservation = Reservation.objects.get(pk=reservation_id)
        return super().form_valid(form)


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "review_list.html"
    queryset = Review.objects.all()

    def get_queryset(self):
        tour_id = int(self.kwargs['id'])
        tour: Tour = Tour.objects.get(pk=tour_id)

        query_set = self.queryset.filter(reservation__tour=tour)

        return query_set

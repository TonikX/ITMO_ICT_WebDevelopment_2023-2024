from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
	path('', views.IndexRedirectView.as_view(), name='home'),

	path('reservations/', views.ReservationListView.as_view(), name='reservations'),
	path('reservation/<int:pk>/delete/', views.ReservationDeleteView.as_view(), name='reservation-delete'),

	path('flights/', views.FlightListView.as_view(), name='flights'),
	path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight-detail'),

	path('flights/<int:pk>/seats/', views.FlightSeatsDetailView.as_view(), name='flight-seats'),

	path('flights/<int:pk>/reviews/', views.ReviewListView.as_view(), name='reviews-list'),
	path('flights/<int:pk>/reviews/create/', views.ReviewCreateView.as_view(), name='review-create'),
	path('reviews/<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='review-edit'),
	path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),

	path('ticket/<int:pk>/book/', views.TicketBookView.as_view(), name='ticket-book'),
]

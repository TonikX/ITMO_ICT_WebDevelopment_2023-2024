from django.urls import path
from . import views
from .views import FlightDetailView, UserRegisterView, TicketBookNewView, TicketDeleteView, TicketUpdateView, AddCommentView

urlpatterns = [
   path('', views.HomeSortView, name="home"),
   path('flight/<int:pk>', FlightDetailView.as_view(), name="flight-detail"),
   path('flight/<int:flight_id>/seats', views.SeatsView, name='seats'),
   path('user/<int:user_id>', views.UserWithFlightsView, name="user-page"),
   path('flight/<int:flight_id>/tickets', views.TicketFlightTableView, name='ticket-table'),
   #path('flight/<int:flight_id>/booking', TicketBookView.as_view(), name='booking'),
   path('flight/<int:flight_id>/seats/<str:seat_id>', TicketBookNewView.as_view(), name='booking-seat'),
   path('user/<int:user_id>/<int:pk>/delete', TicketDeleteView.as_view(), name='delete-ticket'),
   path('user/<int:user_id>/<int:pk>/update', TicketUpdateView.as_view(), name='update-ticket'),
   path('flight/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),


   path('register/', UserRegisterView.as_view(), name='register'),
]

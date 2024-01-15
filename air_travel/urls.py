from django.urls import path
from air_travel import views

urlpatterns = [
    path('', views.Main.as_view(), name='main_page'),
    path('register/', views.RegisterPassenger.as_view(), name='register'),
    path('login/', views.AuthUser.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('profile/', views.UserProfile.as_view(), name='profile'),

    path('edit_booking/<int:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<int:pk>/', views.DeleteBooking.as_view(), name='delete_booking'),
    path('detail_flight/<int:pk>/', views.DetailFlight.as_view(), name='detail_flight'),
    path('detail_flight_for_booking/<int:pk>/', views.DetailFlightForBooking.as_view(),
         name='detail_flight_for_booking'),
]

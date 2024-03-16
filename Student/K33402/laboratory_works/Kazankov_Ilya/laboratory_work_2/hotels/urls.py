from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('hotels/', views.hotels, name='hotels'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('hotelpage/<str:hotel_name>/', views.hotelpage, name='hotelpage'),
    path('booking/<str:hotel_name>/<str:room_category>/', views.booking, name='booking'),
    path('editbooking/<str:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancelbooking/<str:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('review/<str:booking_id>/', views.review, name='review'),
]

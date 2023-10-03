"""
URL configuration for hotelapp.
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('hotel/<id>/', views.hotel, name='hotel'),
    path('room/<id>/', views.room, name='room'),
    path('cancelbooking/<id>/', views.cancelbooking, name='cancelbooking'),
    path('review/<booking_id>/', views.review, name='review'),
    path('account/', views.account, name='account'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

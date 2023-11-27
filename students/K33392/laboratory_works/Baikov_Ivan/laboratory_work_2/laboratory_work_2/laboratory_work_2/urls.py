from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from hotel_list import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('register/', views.register, name='register'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/<int:hotel_id>/review/', views.leave_review, name='leave_review'),
    path('hotel/<int:hotel_id>/reserve/', views.make_reservation, name='make_reservation'),
    path('reservation_confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
    path('admin/', admin.site.urls),
    path('last_month_guests/', views.last_month_guests, name='last_month_guests'),
    path('admin_login/', LoginView.as_view(), name='login'),
    path('admin_logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservation/<int:reservation_id>/cancel/', views.cancel_reservation, name='cancel_reservation'),

]

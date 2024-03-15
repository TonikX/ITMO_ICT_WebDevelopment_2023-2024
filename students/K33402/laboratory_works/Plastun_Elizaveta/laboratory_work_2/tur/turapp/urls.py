from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_tours', views.my_tours, name='my_tours'),
    path('tour/<int:tour_id>', views.tour_page, name='tour_page'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('tour/<int:tour_id>/create_reservation/', views.create_reservation, name='create_reservation'),
    path('tour/<int:tour_id>/delete_reservation/', views.delete_reservation, name='delete_reservation'),
    path('tour/<int:reservation_id>/access_reservation_admin/', views.access_reservation_admin, name='access_reservation_admin'),
    path('tour/<int:reservation_id>/delete_reservation_admin/', views.delete_reservation_admin, name='delete_reservation_admin'),
    path('tour/<int:reservation_id>/cancel_reservation_admin/', views.cancel_reservation_admin, name='cancel_reservation_admin'),
    path('create_tour/', views.create_tour, name='create_tour'),
    path('<int:tour_id>/delete_tour/', views.delete_tour, name='delete_tour'),
    path("register/", views.register, name="register"),
    path('login/', views.LoginView, name='login'),
    path("logout/", views.user_logout, name="logout"),
]
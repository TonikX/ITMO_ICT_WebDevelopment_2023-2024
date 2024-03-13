from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('agency/', views.tour_list, name='tour_list'),
    path('', views.index, name='index'),
    path('agency/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('agency/<int:tour_id>/reserve/', views.reserve_tour, name='reserve_tour'),
    path('agency/<int:tour_id>/comment/', views.add_review, name='add_review'),
    path('tours_by_country/', views.tours_by_country_view, name='tours_by_country'),
]

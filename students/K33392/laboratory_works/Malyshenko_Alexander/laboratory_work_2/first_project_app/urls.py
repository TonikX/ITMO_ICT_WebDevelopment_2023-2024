from django.urls import path
from . import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('users/<int:user_id>/', views.get_user),
    path('races/', views.get_races),
    path('logout/', login_required(views.logout_user)),
    path('registration/', views.registration),
    path('racer_register/', login_required(views.racer_registration)),
    path('login/', views.sign_in),
    path('races/<int:race_id>/', views.get_race),
    path('races/<int:race_id>/registerForRace', login_required(views.register_for_race)),
    path('races/<int:race_id>/unregisterForRace', login_required(views.unregister_for_race)),
    path('races/<int:race_id>/comment', login_required(views.commentCreate))
]

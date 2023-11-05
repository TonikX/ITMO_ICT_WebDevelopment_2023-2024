from django.urls import path
from .views import home, register_user, login_user, race_list, race_detail, registration_list, DeleteRegistration, \
    racer_profile, race_registration, add_comment, custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('races/', race_list, name='race_list'),
    path('races/race/<int:race_id>/', race_detail, name='race_detail'),
    path('registrations/', registration_list, name='registration_list'),
    path('registrations/registration/delete/<int:pk>', DeleteRegistration.as_view()),
    path('racer_profile/', racer_profile, name='racer_profile'),
    path('race_registration/', race_registration, name='race_registration'),
    path('races/race/add_comment/<int:race_id>/', add_comment, name='add_comment'),
]

from django.urls import path
from .views import home, register_user, login_user, race_list, race_detail, registration_list, DeleteRegistration, \
    racer_profile, race_registration

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('races/', race_list, name='race_list'),
    path('races/race/<int:race_id>/', race_detail, name='race_detail'),
    path('registrations/', registration_list, name='registration_list'),
    path('registrations/registration/delete/<int:pk>', DeleteRegistration.as_view()),
    path('racer_profile/', racer_profile, name='racer_profile'),
    path('race_registration/', race_registration, name='race_registration'),
]

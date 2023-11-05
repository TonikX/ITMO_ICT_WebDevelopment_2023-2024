from django.urls import path
from .views import home, register_user, login_user, race_list, race_detail, registration_list, DeleteRegistration

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('races/', race_list, name='race_list'),
    path('races/race/<int:race_id>/', race_detail, name='race_detail'),
    path('registrations/', registration_list, name='registration_list'),
    path('registrations/registration/delete/<int:pk>', DeleteRegistration.as_view()),
]

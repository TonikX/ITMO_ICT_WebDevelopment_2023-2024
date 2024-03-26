from django.urls import path
from . import views

urlpatterns = [
    path('', views.conferences),
    path('logout/', views.logout_user),
    path('register/', views.register_user),
    path('save_registration/', views.save_registration),
    path('my_registrations/', views.my_registrations),
    path('my_registrations/save_registration/', views.update_registration),
    path('my_registrations/cancel_registration/', views.cancel_registration),
    path('save_review/', views.save_review),
    path('participants/', views.participants)
]
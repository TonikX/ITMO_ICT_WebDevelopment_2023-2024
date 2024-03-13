from django.urls import path

from apps.homework import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]

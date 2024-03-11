"""part1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:owner_id>/', views.owner_details),
    path('owners_list/', views.list_owners_view),
    path('cars_list/', views.CarListView.as_view()),
    path('car/<int:pk>/', views.CarDetailView.as_view()),
    path('create_owner/', views.create_owner_view),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/create/', views.CarCreateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
    path("register/", views.register)
]

"""
URL configuration for weblab2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
]


from django.urls import path
from tour_project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.tour_list, name='tour_list'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:tour_id>/reserve/', views.reserve_tour, name='reserve_tour'),
    path('tour/<int:tour_id>/write_review/', views.write_review, name='write_review'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    # URL-маршруты для обновления и удаления резерваций
    path('reservation/update/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('reservation/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('sold_tours_by_country/', views.sold_tours_by_country, name='sold_tours_by_country'),
]

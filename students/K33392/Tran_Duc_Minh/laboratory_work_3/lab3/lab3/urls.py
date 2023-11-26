from django.contrib import admin
from django.urls import path, include, re_path
from tdeeapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>/', UserDetailView.as_view()),

    path('api/activities/', ActivityView.as_view()),
    path('api/activities/<int:pk>/', ActivityDetailView.as_view()),

    path('api/foods/', FoodView.as_view()),
    path('api/foods/<int:pk>/', FoodDetailView.as_view()),

    path('api/profiles/', ProfileView.as_view()),
    path('api/profiles/<int:pk>/', ProfileDetailView.as_view()),

    path('api/daily-data/', DailyDataView.as_view()),
    path('api/daily-data/<int:pk>/', DailyDataDetailView.as_view()),

    path('api/user-foods/', UserFoodView.as_view()),
    path('api/user-foods/<int:pk>/', UserFoodDetailView.as_view()),
]

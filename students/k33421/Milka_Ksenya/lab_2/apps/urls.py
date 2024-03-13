from django.urls import path, include

urlpatterns = [
    path('', include('apps.homework.urls')),
    path('', include('apps.user.urls')),
]

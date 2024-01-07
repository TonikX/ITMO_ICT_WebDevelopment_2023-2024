from django.urls import path, include
from django.contrib import admin
from hotel.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('hotel.urls')),
]

from django.contrib import admin #9
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotels.urls')), #10
]
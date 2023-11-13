"""
URL configuration for myproject project.

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

# C:\WEBDJANGO\myproject\myproject\urls.py
from django.contrib import admin
from django.urls import include, path
from myapp.views import tour_list  
from myapp.views import tour_list, register, login 

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tour_list, name='tour_list'), 
    path('', include('myapp.urls')),
    path('myapp/', include('myapp.urls')), 
    path('register/', register, name='register'),  
    path('login/', login, name='login'), 
]





"""
URL configuration for hotelProject project.

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
from hotel_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('<str:hotel_name>/', views.owner_detail),
    path('user', views.user_log_sign_page, name="userloginpage"),
    path('user/login', views.user_log_sign_page, name="userloginpage"),
    path('staff/login', views.staff_log_sign_page, name="staffloginpage"),
    path('logout', views.logoutuser, name="logout"),

    path('admin/', admin.site.urls),
]

"""
URL configuration for warriors_project project.

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

from warriors.views import *


app_name = "warriors_app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("skills/", SkillList.as_view(), name="skill-list"),
    path("warriors/", WarriorList.as_view(), name="warrior-list"),
    path("warriors/<int:pk>/", WarriorDetail.as_view(), name="warrior-detail"),
]

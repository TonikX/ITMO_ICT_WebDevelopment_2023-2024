"""
URL configuration for simple_drf_project project.

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
from warriors_app.views import SkillListView, WarriorProfessionInfoView, WarriorSkillInfoView, SingleWarriorInfoView, WarriorDeleteView, WarriorUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('warrior_prof_info/', WarriorProfessionInfoView.as_view(), name='warrior_prof_info'),
    path('warrior_skill_info/', WarriorSkillInfoView.as_view(), name='warrior_skill_info'),
    path('warriors/<int:id>/', SingleWarriorInfoView.as_view(), name='single-warrior-info'),
    path('warriors/delete/<int:id>/', WarriorDeleteView.as_view(), name='delete-warrior'),
    path('warriors/update/<int:id>/', WarriorUpdateView.as_view(), name='update-warrior'),
]

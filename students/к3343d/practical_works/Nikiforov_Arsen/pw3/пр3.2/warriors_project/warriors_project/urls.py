# warriors_project/urls.py
from django.contrib import admin
from django.urls import path, include
from warriors_app.views import WarriorWithProfessionAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warriors_app.urls', namespace='warriors_app_namespace')),
    path('warriors-with-professions/', WarriorWithProfessionAPIView.as_view(), name='warriors_with_professions'),
]

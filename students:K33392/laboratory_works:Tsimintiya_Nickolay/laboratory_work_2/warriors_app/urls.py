from django.urls import path
from .views import WarriorAPIView

app_name = "warriors_app"

urlpatterns = [
    path("warriors/", WarriorAPIView.as_view())
]
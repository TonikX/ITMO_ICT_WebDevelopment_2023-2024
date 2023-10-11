from django.urls import path
from . import views # подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    path('owner/<int:id>/', views.detail),
]
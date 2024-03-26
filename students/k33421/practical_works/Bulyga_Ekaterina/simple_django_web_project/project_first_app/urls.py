from django.urls import path
from . import views

urlpatterns = [
    path('owner/', views.detail),
    path('car/', views.AutoList.as_view()),
    path('form/', views.ownerForm),
    path('create/', views.CarCreateForm.as_view(success_url='/create/'))
]
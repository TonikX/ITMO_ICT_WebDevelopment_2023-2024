from django.urls import path
from .views import *

urlpatterns = [
        path('owner/<int:owner_id>/', detail),
        path("cars", CarListView.as_view()),
        path("cars/<int:pk>", CarDetailView.as_view()),
        path("cars/<int:pk>/update", CarUpdateView.as_view()),
        path("cars/<int:pk>/delete", CarDeleteView.as_view()),
        path("cars/create", CarCreateView.as_view()),
        path("owners", owner_list, name = "owner_list"),
        path("owners/<int:owner_id>", owner_get),
        path("owners/create", owner_create)
]


from django.urls import path
from . import views

urlpatterns = [
    path("owners/<int:id>", views.detail),
    path("owners", views.get_all_owners),
    path("cars", views.CarListView.as_view()),
    path("cars/<int:pk>/update", views.UpdateCardView.as_view()),
    path("register", views.CreateUserView.as_view())
]
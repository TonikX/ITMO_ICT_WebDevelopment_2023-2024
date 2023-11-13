from django.urls import path
from . import views
from . import forms


urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail),
    path('owner/list/', views.owners_list_view),
    path('owner/create', views.create_owner_view),
    path('car/list/', views.CarListView.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/create/', views.CarCreate.as_view(success_url="/car/list/")),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]


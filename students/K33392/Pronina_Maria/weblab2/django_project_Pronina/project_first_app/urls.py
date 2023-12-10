from django.urls import path
from . import views


urlpatterns = [
    path('owner/<owner_id>/', views.get_owner),
    path('cars/<car_id>/', views.get_car_owners),
    path('allowners/', views.get_owners),
    path('car/list', views.CarList.as_view()),
    path('car/<int:pk>', views.CarById.as_view()),
    path('new_owner', views.owner_form_view),
    path('update_car/<int:pk>', views.CarUpdateView.as_view()),
    path('new_car', views.CarCreateView.as_view()),
    path('delete_car/<int:pk>', views.CarDeleteView.as_view()),
]
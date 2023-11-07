from django.urls import path

from students.K33391.practical_works.Ким_Даниил.simple_django_web_project.django_project_Kim.project_first_app import \
    views

urlpatterns = [
    path('owners/<int:car_owner_id>', views.car_owner_detail),
    path('owners', views.car_owners_list_view),
    path('cars', views.CarsList.as_view()),
    path('cars/<int:car_id>', views.car_detail),
]
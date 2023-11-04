from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homeworks', views.homeworks, name='homeworks'),
    path('marks', views.marks, name='marks'),
    path('solution/<int:homework_id>', views.add_solution, name='add_solution'),
]
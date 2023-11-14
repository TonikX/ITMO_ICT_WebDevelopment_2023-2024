from django.urls import path 
from . import views # подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    path('owner/<int:id>/', views.detail), # пример вызова контроллера (функции) с именем "special_case_200" из файда views
    path('time/', views.example_view),
    path('example_list/', views.list_view),
    path('сvb_example/', views.ExampleList.as_view()),
    path('publisher/<int:pk>/', views.PublisherRetrieveView.as_view()),
    path('book/list/', views.BookListView.as_view()),
    path('example_create/', views.create_view),
    path('publisher/<int:pk>/update/', views.PublisherUpdateView.as_view()),
    path('cvb_example_create', views.ExampleCreate.as_view(success_url="/сvb_example/")),
    path('publisher/create/', views.PublisherUpdateView.as_view()),
    path('publisher/<int:pk>/delete/', views.PublisherDeleteView.as_view()),
]
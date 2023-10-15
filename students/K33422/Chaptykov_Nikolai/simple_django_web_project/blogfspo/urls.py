"""blogfspo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:owner_id>/', views.detail),
    path('date/', views.getDate),
    path('example_list/', views.listView),
    path('сvb_example/', views.ExampleList.as_view()),
    path('publisher/<int:pk>/', views.PublisherRetrieveView.as_view()),
    path('book/list/', views.BookListView.as_view()),
    path('cars/', views.CarListView.as_view()),
    path('persons/', views.PersonListView),
    path('example_create', views.create_view),
    path('publisher/<int:pk>/update/', views.PublisherUpdateView.as_view()),
    path('cvb_example_create', views.ExampleCreate.as_view(success_url="/сvb_example/")),
    path('publisher/create/', views.PublisherCreateView.as_view()),
    path('publisher/<int:pk>/delete/', views.PublisherDeleteView.as_view()),
    path('person_create', views.PostPerson),
    path('car_create', views.CarCreate.as_view()),
    path('car_update/<int:pk>/', views.CarUpdate.as_view()),
    path('car_delete/<int:pk>/', views.CarDelete.as_view()),
    path('car_detail/<int:pk>/', views.CarDetail.as_view()),
    path('update_profile/', views.update_profile)
]

from django.urls import path
from .views import create_view
# importing views from views..py
from .views import ExampleList
from .views import list_view
from .views import OwnerListView
from . import views # Подключение файла контроллеров, описанного в приложении
# urls.py
from django.urls import path
from .views import create_owner
from .views import CarCreateView, CarUpdateView, CarDeleteView
from .views import CarListView, create_car



urlpatterns = [
    path('example_list/', list_view, name='example_list'),
    path('example/', ExampleList.as_view(), name='example_list_view'),
    path('owners/', views.owner_list, name='owner_list'),
    path('cars/', views.car_list, name='car_list'),
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owner/list/', OwnerListView.as_view(), name='owner_list_view'),
    path('example_create', create_view),
    path('car/list/', views.CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='update_car'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car'),
    path('car/create/', create_car, name='create_car'),
    path('owner/create/', create_owner, name='create_owner'),
    


]




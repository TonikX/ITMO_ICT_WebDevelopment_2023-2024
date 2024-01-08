from django.urls import path

from .views import *

urlpatterns = [
	path('owner/<int:owner_id>', owner_detail, name='owner_detail'),
	path('owners/', owner_list, name='owner_list'),
	path('car/<int:pk>', CarDetail.as_view(), name='car_detail'),
	path('cars/', CarList.as_view(), name='car_list'),
	path('owner_create/', owner_create, name='owner_create'),
	path('car_create/', CarCreate.as_view(), name='car_create'),
	path('car_update/<int:pk>', CarUpdate.as_view(), name='car_update'),
	path('car_delete/<int:pk>', CarDelete.as_view(), name='car_delete'),
]

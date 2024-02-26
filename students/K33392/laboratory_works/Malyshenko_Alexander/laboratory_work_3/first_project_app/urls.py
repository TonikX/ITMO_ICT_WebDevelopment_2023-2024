from .views import *
from django.urls import path

urlpatterns = [
    path('items/', ItemAPIView.as_view()),
    path('items/add/', ItemCreateAPIView.as_view()),
    path('items/<int:pk>/', ItemDetailAPIView.as_view()),
    path('warehouses/', WarehousesListAPIView.as_view()),
    path('warehouses/<int:pk>/', WarehouseInventoryAPIView.as_view()),
    path('shipments/', ShipmentsListAPIView.as_view()),
    path('shipments/<int:pk>', ShipmentDetailAPIView.as_view()),
    path('shipments/<int:pk>/comments', CommentsListAPIView.as_view()),
    path('shipments/comments/add', CommentCreateAPIView.as_view()),
    path('shipments/create/warehouse/<int:pk>', ShipmentCreateAPIView.as_view())
]

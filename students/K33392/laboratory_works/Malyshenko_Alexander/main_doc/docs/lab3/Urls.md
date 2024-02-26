## Роутеры

### **В лабораторной работе были использованы следующие роутеры:**

#### Получение данных о продметах / предмете и добавление нового предмета:
```py
    path('items/', ItemAPIView.as_view()),
    path('items/add/', ItemCreateAPIView.as_view()),
    path('items/<int:pk>/', ItemDetailAPIView.as_view()),
```

#### Полечение данных о складах и списка предметов конкретного склада:
```py
    path('warehouses/', WarehousesListAPIView.as_view()),
    path('warehouses/<int:pk>/', WarehouseInventoryAPIView.as_view()),
```

#### Информация о отгрузках, создание новой отгрузки, создание коментариев к отгрузке
```py
    path('shipments/', ShipmentsListAPIView.as_view()),
    path('shipments/<int:pk>', ShipmentDetailAPIView.as_view()),
    path('shipments/<int:pk>/comments', CommentsListAPIView.as_view()),
    path('shipments/create/warehouse/<int:pk>', ShipmentCreateAPIView.as_view()
```
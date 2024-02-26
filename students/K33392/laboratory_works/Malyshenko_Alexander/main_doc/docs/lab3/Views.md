## Представления

### Представления для предметов
```py
class ItemAPIView(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Item.objects.all()
```
Для получения списка всех прдеметов.

```py
class ItemDetailAPIView(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        nomenclature = Nomenclature.objects.filter(item_id=item)
        item_serializer = ItemsSerializer(item)
        nomenclature_serializer = NomenclatureSerializer(nomenclature, many=True)
        return Response({"Items": item_serializer.data, 'Nomenclature': nomenclature_serializer.data})
```
Для получения информации о конкретном предмете.

```py
class ItemCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ItemsSerializer
    queryset = Item.objects.all()
```
Для создания нового предмета.

### Представления складов
```py
class WarehousesListAPIView(generics.ListAPIView):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
```
Для получения списка складов.

```py
class WarehouseInventoryAPIView(generics.ListAPIView):
    serializer_class = WarehouseInventorySerializer

    def get_queryset(self):
        warehouse_id = self.kwargs.get('pk', None)
        queryset = Nomenclature.objects.filter(warehouse_id=warehouse_id)
        return queryset
```
Для получения списка предметов на конкретном складе.

### Представления для отгрузки
```py
class ShipmentsListAPIView(generics.ListAPIView):
    serializer_class = ShipmentListSerializer
    queryset = Shipment.objects.all()
```
Для получения списка всех отгрузок.

```py
class ShipmentCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get(self, request, pk):
        warehouse_nom = Nomenclature.objects.filter(warehouse_id=pk)
        warehouse = Warehouse.objects.get(pk=pk)
        nomenclature_serializer = WarehouseInventorySerializer(warehouse_nom, many=True)
        return Response((f"{warehouse.name} items", nomenclature_serializer.data))

    def post(self, request, pk):
        data = request.data.copy()
        nomenclature = Nomenclature.objects.filter(warehouse_id=pk, item_id=int(data['item_id'])).first()
        if nomenclature is None:
            return Response("No such item in warehouse")

        if float(data['amount']) > nomenclature.amount:
            return Response("Not enough items in stock")

        if data['old_warehouse_id'] == data['new_warehouse_id']:
            return Response("You cannot move an item to the same warehouse")

        data['datetime'] = datetime.now()
        shipment_serializer = ShipmentSerializer(data=data)
        if shipment_serializer.is_valid(raise_exception=True):
            shipment_serializer.save()
            old_nomenclature = nomenclature
            old_nomenclature.amount -= float(data['amount'])
            new_nomenclature = Nomenclature.objects.filter(warehouse_id=int(data['new_warehouse_id']),
                                                           item_id=int(data['item_id'])).first()
            if new_nomenclature is None:
                new_nomenclature = Nomenclature(
                    item_id=Item.objects.get(pk=int(data['item_id'])),
                    warehouse_id=Warehouse.objects.get(pk=int(data['new_warehouse_id'])),
                    name="",
                    amount=float(data['amount'])
                )
            else:
                new_nomenclature.amount += float(data['amount'])

            old_nomenclature.save()
            new_nomenclature.save()
            return Response(shipment_serializer.data)

        return Response(shipment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
Для отгрузки конкретного товара.

```py
class ShipmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentListSerializer
```
Для получения информации о конкретной отгрузке.

### Представление для создания комментария
```py
def register_for_race(request, race_id):
    race_object = Race.objects.get(pk=race_id)
    if race_object.winner_id is not None:
        return redirect('/races')

    if not request.user.is_authenticated:
        return redirect('/races')

    user = User.objects.get(pk=request.user.id)
    racer = Racer.objects.get(user_id=user)
    stats = Statistic.objects.filter(race_id=race_object) & Statistic.objects.filter(user_id=racer)
    if stats.count() > 0:
        return redirect('/races')

    stats = Statistic.objects.create(user_id=racer, race_id=race_object)
    return redirect('/races/' + str(race_object.id))
``` 
Представление регистрирует авторизованного гонщика как участника выбранной гонки.

### Представление для удаления регистрации гонщиков на гонку
```py
def unregister_for_race(request, race_id):
    race_object = Race.objects.get(pk=race_id)
    if race_object.winner_id is not None:
        return redirect('/races')

    if not request.user.is_authenticated:
        return redirect('/races')

    user = User.objects.get(pk=request.user.id)
    racer = Racer.objects.get(user_id=user)
    stats = Statistic.objects.filter(race_id=race_object) & Statistic.objects.filter(user_id=racer)
    if stats.count() <= 0:
        return redirect('/races')

    stats.delete()
    return redirect('/races/' + str(race_object.id))
```
Представление противоположное предыдущему.
Удаляет регистрацию авторизованного гонщика из выбранной гонки.

### Представление для создания новых комментариев и их получения
```py
class CommentsListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
```
Для получения всех коментариев отгрузки
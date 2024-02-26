# Сериалайзеры

## **Обычные сериалайзеры:**
##### Сериалайзер со всеми полями прдеметов:
``` py
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

##### Сериалайзер с некоторыми полями прдеметов:
``` py
class NotFullItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'item_barcode', 'measurement_unit']
```

##### Сериалайзер с полями номенклатуры, отображающими номер склада и количество:
``` py
class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = ['warehouse_id', 'amount']
```

##### Сериалайзер со всеми полями склада:
``` py
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
```

##### Сериалайзер с определенными полями отгрузки:
``` py
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['user_id', 'item_id', 'amount', 'old_warehouse_id', 'new_warehouse_id']

```

##### Сериалайзер со всеми полями комментариев:
``` py
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

```

## **Сложные сериалайзеры:**
##### Сериалайзер с информацией о номенлкатуре, где вместо ```item_id``` наследуется сериалайзер товара:
``` py
class WarehouseInventorySerializer(serializers.ModelSerializer):
    item_id = NotFullItemsSerializer()

    class Meta:
        model = Nomenclature
        fields = ['item_id', 'name', 'amount']
```

##### Сериалайзер с информацией о номенлкатуре, где вместо ```item_id``` наследуется сериалайзер товара, а вместо ```old_warehouse_id``` и ```new_warehouse_id``` наследуется сериалайзер слкада:
``` py
class ShipmentListSerializer(serializers.ModelSerializer):
    item_id = NotFullItemsSerializer()
    old_warehouse_id = WarehouseSerializer()
    new_warehouse_id = WarehouseSerializer()

    class Meta:
        model = Shipment
        fields = '__all__'
```
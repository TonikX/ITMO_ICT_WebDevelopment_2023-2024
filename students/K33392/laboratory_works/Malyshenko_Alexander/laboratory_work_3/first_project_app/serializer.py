from rest_framework import serializers
from .models import *


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class NotFullItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'item_barcode', 'measurement_unit']


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = ['warehouse_id', 'amount']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseInventorySerializer(serializers.ModelSerializer):
    item_id = NotFullItemsSerializer()

    class Meta:
        model = Nomenclature
        fields = ['item_id', 'name', 'amount']


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['user_id', 'item_id', 'amount', 'old_warehouse_id', 'new_warehouse_id']


class ShipmentListSerializer(serializers.ModelSerializer):
    item_id = NotFullItemsSerializer()
    old_warehouse_id = WarehouseSerializer()
    new_warehouse_id = WarehouseSerializer()

    class Meta:
        model = Shipment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

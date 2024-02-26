import datetime

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *
from .models import *


class ItemAPIView(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Item.objects.all()


class ItemCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ItemsSerializer
    queryset = Item.objects.all()


class ItemDetailAPIView(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        nomenclature = Nomenclature.objects.filter(item_id=item)
        item_serializer = ItemsSerializer(item)
        nomenclature_serializer = NomenclatureSerializer(nomenclature, many=True)
        return Response({"Items": item_serializer.data, 'Nomenclature': nomenclature_serializer.data})


class WarehousesListAPIView(generics.ListAPIView):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()


class WarehouseInventoryAPIView(generics.ListAPIView):
    serializer_class = WarehouseInventorySerializer

    def get_queryset(self):
        warehouse_id = self.kwargs.get('pk', None)
        queryset = Nomenclature.objects.filter(warehouse_id=warehouse_id)
        return queryset


class ShipmentsListAPIView(generics.ListAPIView):
    serializer_class = ShipmentListSerializer
    queryset = Shipment.objects.all()


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


class CommentsListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ShipmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentListSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

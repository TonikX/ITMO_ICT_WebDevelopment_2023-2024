from rest_framework import serializers
from LR1_secondApp.models import *
from django.contrib.auth.models import User


class DisksSerializers(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.prod_date = validated_data.get('prod_date', instance.prod_date)
        instance.firm = validated_data.get('firm', instance.firm)
        instance.save()
        return instance

    class Meta:
        model = Disks
        fields = ("id", "prod_date", "firm")


class GamesSerializers(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.author = validated_data.get('author', instance.author)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.save()
        return instance

    class Meta:
        model = Games
        fields = ("id", "name", "type", "author", "disk")


class SaleSerializers(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.sale_date = validated_data.get('sale_date', instance.sale_date)
        instance.sale_quantity = validated_data.get('sale_quantity', instance.sale_quantity)
        instance.sale_price = validated_data.get('sale_price', instance.sale_price)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.save()
        return instance

    class Meta:
        model = Sale
        fields = ("id", "sale_date", "sale_quantity", "disk", "sale_price")


class AdmissionSerializers(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.admission_date = validated_data.get('admission_date', instance.admission_date)
        instance.admission_quantity = validated_data.get('admission_quantity', instance.admission_quantity)
        instance.admission_price = validated_data.get('admission_price', instance.admission_price)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.save()
        return instance

    class Meta:
        model = Admission
        fields = ("id", "admission_date", "admission_quantity", "disk", "admission_price")


class Sale_pointSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale_point
        fields = ("id", "sale_point_name", "sale_point_address", "number_of_stuff", "sale_id")


class Admission_pointSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admission_point
        fields = ("id", "admission_point_name", "admission_point_address", "number_of_stuff", "admission_id")


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

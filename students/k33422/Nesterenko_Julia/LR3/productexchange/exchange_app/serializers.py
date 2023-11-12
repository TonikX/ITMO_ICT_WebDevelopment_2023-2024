from rest_framework import serializers
from .models import *


# Cериализатор производителя
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


# Cериализатор типа товара
class ProductTypeSerializer(serializers.ModelSerializer):
    units = serializers.ChoiceField(choices=ProductType.units_types)

    class Meta:
        model = ProductType
        fields = "__all__"


# Cериализатор брокера
class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = "__all__"


# Cериализатор товара для просмотра
class ProductSerializer(serializers.ModelSerializer):
    type = ProductTypeSerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = "__all__"


# Cериализатор товара для создания/редактирования
class ProductEditableSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=ProductType.objects.all())
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Product
        fields = "__all__"


# Cериализатор партии для просмотра
class ConsignmentSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Consignment
        fields = "__all__"


# Cериализатор партии для просмотра усеченный
class ConsignmentReducedSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer()

    class Meta:
        model = Consignment
        exclude = ["products"]


# Cериализатор партии для создания/редактирования
class ConsignmentEditableSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Consignment.status_types)
    terms = serializers.ChoiceField(choices=Consignment.terms_types)
    broker = serializers.PrimaryKeyRelatedField(queryset=Broker.objects.all())

    class Meta:
        model = Consignment
        exclude = ["products"]


# Cериализатор товара в партии для просмотра
class ProductInConsignmentSerializer(serializers.ModelSerializer):
    consignment = ConsignmentReducedSerializer()
    product = ProductSerializer()

    class Meta:
        model = ProductInConsignment
        fields = "__all__"


# Cериализатор товара в партии для создания/редактирования
class ProductInConsignmentEditableSerializer(serializers.ModelSerializer):
    consignment = serializers.PrimaryKeyRelatedField(queryset=Consignment.objects.filter(status='a'))
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductInConsignment
        fields = "__all__"
import datetime

from rest_framework import serializers
from .models import Consignment, Company, BrokerCompany, Broker, ProductByCompany, Product


class ProductSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CountProductSerialiser(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["count"]

    def get_count(self, obj):
        return ProductByCompany.objects.filter(product=obj.id, created__lt=self.context["date"]).count()


class DateSerializer(serializers.Serializer):
    date = serializers.DateField(default=datetime.date.today())

    class Meta:
        fields = ['date']


class ProductByCompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = ProductByCompany
        fields = "__all__"


class CompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class BrokerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = "__all__"


class CountBrokerSalarySerializer(serializers.ModelSerializer):

    salary = serializers.SerializerMethodField()

    class Meta:
        model = Broker
        fields = ['id', 'name', 'salary']

    def get_salary(self, obj):
        count = 0
        for c in Consignment.objects.filter(broker=obj.id):
            count = ProductByCompany.objects.filter(consignment=c.id).count() * c.cost
        return count


class BrokerCompanySerialiser(serializers.ModelSerializer):
    class Meta:
        model = BrokerCompany
        fields = "__all__"


class ConsignmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Consignment
        fields = "__all__"

class BrokerWithCompanySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Broker
        fields = ['id', 'name', 'income', 'company', 'company_name']


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

class BrokerTopProductsSerializer(serializers.ModelSerializer):
    top_products = serializers.SerializerMethodField()

    class Meta:
        model = Broker
        fields = ['id', 'name', 'top_products']

    def get_top_products(self, obj):
        current_year = self.context['date'].year
        consignments = Consignment.objects.filter(broker=obj.id, date_sold__year=current_year)

        product_counts = {}

        for consignment in consignments:
            products_in_consignment = ProductByCompany.objects.filter(consignment=consignment.id)
            
            for product_by_company in products_in_consignment:
                product = product_by_company.product
                product_count = product_counts.get(product.id, 0)
                product_counts[product.id] = product_count + 1

        sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        top_products_data = []

        for product_id, count in sorted_products:
            product = Product.objects.get(id=product_id)
            top_products_data.append({
                'product_id': product_id,
                'product_name': product.name,
                'count': count,
            })

        return top_products_data

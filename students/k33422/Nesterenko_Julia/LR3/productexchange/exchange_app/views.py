import pytz
from django.db.models import Sum
from rest_framework.views import APIView, Response
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView, RetrieveUpdateAPIView)
from .models import *
from .serializers import *


def localize_isodate(date_string):
    date = datetime.datetime.fromisoformat(date_string)
    return pytz.utc.localize(date)


# Все вью для производителя

class ManufacturerListAPIView(ListAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerCreateAPIView(CreateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerOneAPIView(RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerEditAPIView(RetrieveUpdateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


# Все вью для вида товара

class ProductTypeListAPIView(ListAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeCreateAPIView(CreateAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeOneAPIView(RetrieveAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeEditAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


# Все вью для брокера

class BrokerListAPIView(ListAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


class BrokerCreateAPIView(CreateAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


class BrokerOneAPIView(RetrieveAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


class BrokerDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


class BrokerEditAPIView(RetrieveUpdateAPIView):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


# Все вью для товара

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductEditableSerializer
    queryset = Product.objects.all()


class ProductOneAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductEditAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductEditableSerializer
    queryset = Product.objects.all()


# Все вью для партии

class ConsignmentListAPIView(ListAPIView):
    serializer_class = ConsignmentSerializer
    queryset = Consignment.objects.all()


class ConsignmentCreateAPIView(CreateAPIView):
    serializer_class = ConsignmentEditableSerializer
    queryset = Consignment.objects.all()


class ConsignmentOneAPIView(RetrieveAPIView):
    serializer_class = ConsignmentSerializer
    queryset = Consignment.objects.all()


class ConsignmentDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = ConsignmentSerializer
    queryset = Consignment.objects.all()


class ConsignmentEditAPIView(RetrieveUpdateAPIView):
    serializer_class = ConsignmentEditableSerializer
    queryset = Consignment.objects.all()


# Все вью для товара в партии

class ProductInConsignmentListAPIView(ListAPIView):
    serializer_class = ProductInConsignmentSerializer
    queryset = ProductInConsignment.objects.all()


class ProductInConsignmentCreateAPIView(CreateAPIView):
    serializer_class = ProductInConsignmentEditableSerializer
    queryset = ProductInConsignment.objects.all()


class ProductInConsignmentOneAPIView(RetrieveAPIView):
    serializer_class = ProductInConsignmentSerializer
    queryset = ProductInConsignment.objects.all()


class ProductInConsignmentDeleteAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductInConsignmentSerializer
    queryset = ProductInConsignment.objects.all()


class ProductInConsignmentEditAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductInConsignmentEditableSerializer
    queryset = ProductInConsignment.objects.all()


# Подсчитать, сколько единиц товара каждого вида выставлено на продажу
# от начала торгов до заданной даты
class ProductsByTypeAndDateAPIView(APIView):

    def get(self, request):
        date_from = localize_isodate(request.query_params.get('date_from'))
        date_until = localize_isodate(request.query_params.get('date_until'))
        data = ProductInConsignment.objects.filter(consignment__opening_date__range=(date_from, date_until))\
            .values('product__type__id', 'product__type__name')\
            .annotate(count=Sum('amount')).order_by('-count')
        return Response({"ProductTypeCounts": data})


# Найти фирму-производителя товаров, которая за заданный период времени
# выручила максимальную сумму денег
class TopManufacturerByDateAPIView(APIView):

    def get(self, request):
        date_from = localize_isodate(request.query_params.get('date_from'))
        date_until = localize_isodate(request.query_params.get('date_until'))
        prod_cons = ProductInConsignment.objects.filter(consignment__opening_date__range=(date_from, date_until),
                                                        consignment__status='s')
        pairs = {}
        for pc in prod_cons:
            pairs[pc.product.manufacturer] = (pairs.get(pc.product.manufacturer.name, 0) +
                                              pc.amount*pc.product.price)
        """
        #data = [{"Manufacturer": ManufacturerSerializer(key).data, "Income": value} for key, value in pairs.items()
                if value == max(pairs.values())]
        """
        data = []
        for key, value in pairs.items():
            if value == max(pairs.values()):
                base_dict = ManufacturerSerializer(key).data
                base_dict['income'] = value
                data.append(base_dict)

        return Response({"TopPerformingManufacturer": data})


# Найти товары, которые никогда не выставляли на продажу брокеры заданной конторы
class ProductsNotSoldByCompanyAPIView(APIView):

    def get(self, request):
        company = request.query_params.get('company')
        brokers = Broker.objects.filter(company=company)
        consignments = Consignment.objects.filter(broker__in=brokers)
        sold_products = ProductInConsignment.objects.filter(consignment__in=consignments).values('product_id')
        unsold_products = Product.objects.exclude(pk__in=sold_products)
        serializer = ProductSerializer(unsold_products, many=True)
        return Response({f"ProductsNotSoldBy{company}": serializer.data})


# Найти все факты выставления на продажу товаров с просроченной годностью
class ExpiredProductsAPIView(ListAPIView):
    serializer_class = ProductInConsignmentSerializer
    queryset = [p for p in ProductInConsignment.objects.all()
                if p.consignment.delivery_date > p.product.expiration_date]


# Найти зарплату всех брокеров заданной конторы
class BrokerSalaryByCompanyAPIView(APIView):
    def get(self, request):
        company = request.query_params.get('company')
        queryset = Broker.objects.filter(company=company)
        serializer = BrokerWithSalarySerializer(queryset, many=True)
        return Response({f"BrokersFrom{company}": sorted(serializer.data, key=lambda x: -x["salary"])})

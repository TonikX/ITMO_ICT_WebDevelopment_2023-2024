from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consignment, Company, BrokerCompany, Broker, ProductByCompany, Product
from .serializers import (
    ConsignmentSerialiser,
    CompanySerialiser,
    BrokerCompanySerialiser,
    BrokerSerialiser,
    ProductSerialiser,
    ProductByCompanySerialiser,
    DateSerializer,
    CountBrokerSalarySerializer,
    BrokerTopProductsSerializer,
)
import datetime
from rest_framework.permissions import IsAuthenticated

class ConsignmentViewSet(viewsets.ModelViewSet):
    queryset = Consignment.objects.all()
    serializer_class = ConsignmentSerialiser
    permission_classes = [IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'count_all':
            return DateSerializer
        else:
            return CompanySerialiser

    @action(detail=False, methods=["GET"])
    def sold_most(self, request):
        max_comp = None
        max_val = 0

        for comp in Company.objects.all():
            count = 0
            pbcs = ProductByCompany.objects.filter(company=comp.id)
            for pbc in pbcs:
                count += pbc.consignment.cost

            if count > max_val:
                max_val = count
                max_comp = comp

        return Response({"company": max_comp, "income": max_val})

class BrokerCompanyViewSet(viewsets.ModelViewSet):
    queryset = BrokerCompany.objects.all()
    serializer_class = BrokerCompanySerialiser
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["GET"])
    def never_sold(self, request, pk=None):
        bc = self.get_object()
        sold_qs = Product.objects.filter(produced_by__consignment__broker__company=bc.id).distinct()
        qs = Product.objects.exclude(id__in=sold_qs)
        ser = ProductSerialiser(qs, many=True)
        return Response(ser.data)

    @action(detail=True, methods=["GET"])
    def salaries(self, request, pk=None):
        brokers = Broker.objects.filter(company=pk)
        ser = CountBrokerSalarySerializer(brokers, many=True)
        return Response(ser.data)

class BrokerViewSet(viewsets.ModelViewSet):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerialiser
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["GET"])
    def top_products(self, request, pk=None):
        broker = self.get_object()
        ser = BrokerTopProductsSerializer(broker, context={'date': datetime.date.today()})
        return Response(ser.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['count_all']:
            return DateSerializer
        else:
            return ProductSerialiser

    @action(detail=False, methods=["POST"])
    def count_all(self, request):
        date = request.data['date']
        ser = ProductSerialiser(self.queryset, many=True, context={'date': date})
        return Response(ser.data)

class ProductByCompanyViewSet(viewsets.ModelViewSet):
    queryset = ProductByCompany.objects.all()
    serializer_class = ProductByCompanySerialiser
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def expired(self, request):
        qs = ProductByCompany.objects.none()
        for obj in self.queryset:
            if (obj.consignment.date_sold - obj.created) > datetime.timedelta(days=obj.product.shelf_life):
                qs |= self.queryset.filter(id=obj.id)

        ser = ProductByCompanySerialiser(qs, many=True)
        return Response(ser.data)

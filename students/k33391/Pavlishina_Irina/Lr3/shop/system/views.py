from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiTypes
from rest_framework.permissions import SAFE_METHODS
from . import serializers
from .utils import get_tokens_for_user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Sum
from .models import (CustomUser,
                     Newspaper,
                     Printer,
                     PrintingNewspaper,
                     PostOffice,
                     PostOfficeOrder,
                     Transportation)


class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    queryset = CustomUser.objects.all()


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        print(username, password)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = serializers.LogoutSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

##############################################


class NewspaperViewSet(ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = serializers.NewspaperSerializer


class PostOfficeViewSet(ModelViewSet):
    queryset = PostOffice.objects.all()
    serializer_class = serializers.PostOfficeSerializer


class PrinterViewSet(ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = serializers.PrinterSerializer


class PrintingNewspaperViewSet(ModelViewSet):
    queryset = PrintingNewspaper.objects.all()

    def get_serializer_class(self):
        if self.action in SAFE_METHODS:
            return serializers.ShowPrintingNewspaperSerializer
        return serializers.PrintingNewspaperSerializer


class PostOfficeOrderViewSet(ModelViewSet):
    queryset = PostOfficeOrder.objects.all()

    def get_serializer_class(self):
        if self.action in SAFE_METHODS:
            return serializers.ShowPostOfficeOrderSerializer
        return serializers.PostOfficeOrderSerializer


class TransportationViewSet(ModelViewSet):

    queryset = Transportation.objects.all()

    def get_serializer_class(self):
        if self.action in SAFE_METHODS:
            return serializers.ShowTransportationSerializer
        return serializers.TransportationSerializer


class ActionViewSet(ViewSet):

    @extend_schema(request=OpenApiTypes.STR, responses=serializers.ShowLossSerializer)
    @action(detail=False, methods=['POST'], url_path='more-expensive-newspapers')
    def by_cost(self, request):
        cost =  float(list(request.data.keys())[0])
        gazettes = Newspaper.objects.filter(cost__gt=cost)
        qs = PostOfficeOrder.objects.filter(newspaper__in=gazettes)
        ser = serializers.ShowPostOfficeOrderSerializer(qs, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @extend_schema(responses=serializers.ShowLossSerializer)
    @action(detail=False, methods=['GET'], url_path='lost-delivers')
    def errors(self, request, pk=None):
        qs = Transportation.objects.none()
        context = {}

        for obj in PostOffice.objects.all():
            for journal in PostOfficeOrder.objects.filter(post_office=obj.id):
                sum = Transportation.objects.filter(post_office_order__post=obj.id,
                                                    post_office_order_newspaper=journal.id).aggregate(Sum('amount'))
                if sum['amount__sum'] < journal.amount:
                    qs |= PostOfficeOrder.objects.filter(id=journal.id)
                    context[journal.id] = sum

        ser = serializers.ShowLossSerializer(qs, many=True, context=context)
        return Response(ser.data, status=status.HTTP_200_OK)

    @extend_schema(request=OpenApiTypes.STR, responses=serializers.ShowLossSerializer)
    @action(detail=False, methods=['POST'], url_path='find-addresses')
    def find_by_name(self, request):
        name = list(request.data.keys())[0]
        qs = PrintingNewspaper.objects.filter(newspaper__name=name)
        ser = serializers.ShowPrintingAddreses(qs, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)

    @extend_schema(request=serializers.FindTransportationsSerializers,
                   responses=serializers.ShowTransportEndSerializer)
    @action(detail=False, methods=['POST'], url_path='where-to-sell')
    def where_to_sell(self, request):
        name = request.data['name']
        address = request.data['where_printed']
        gip = PrintingNewspaper.objects.filter(newspaper__name=name, printer__address=address).first()
        obj = Transportation.objects.filter(printing_newspaper=gip.id).first()
        ser = serializers.ShowTransportEndSerializer(obj)
        return Response(ser.data, status=status.HTTP_200_OK)

    @extend_schema(responses={
        'most-sold-redactor': serializers.ShowRedactor,
        'printed_here': OpenApiTypes.INT,
        'show_printed': serializers.ShowPrintingNewspaperSerializer(many=True),
        'where-to-sell': serializers.ShowTransportEndSerializer(many=True)
    })
    @action(detail=True, methods=['GET'], url_path='report')
    def redactor(self, request, pk=None):
        data = {}

        obj = PrintingNewspaper.objects.filter(printer=pk).order_by('-how_many_to_print').first()

        if obj:
            ser = serializers.ShowRedactor(obj.newspaper)
            data['most-sold-redactor'] = ser.data
        else:
            data['most-sold-redactor'] = {}

        qs = PrintingNewspaper.objects.filter(printer=pk)

        data['printed_here'] = qs.count()

        ser = serializers.ShowPrintingNewspaperSerializer(qs, many=True)
        data['show_printed']  = ser.data

        ts = Transportation.objects.filter(printing_newspaper__in=qs)
        ser = serializers.ShowTransportEndSerializer(ts, many=True)
        data['where-to-sell'] = ser.data

        return Response(data, status=status.HTTP_200_OK)


